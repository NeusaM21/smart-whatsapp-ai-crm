from fastapi import FastAPI
# Importar o router da rota de saúde (Health Check)
from app.routes.health import router as health_router 
# NOVO: Importar o router da rota do WhatsApp
from app.routes.whatsapp import router as whatsapp_router 


app = FastAPI(
    title="Smart WhatsApp AI CRM",
    description="Virtual assistant, sales automation and CRM with AI",
    version="0.1.0"
)

# Incluir o router de saúde (já estava correto)
app.include_router(health_router, tags=["Health"]) 
# NOVO: Incluir o router do WhatsApp
app.include_router(whatsapp_router, tags=["WhatsApp & CRM"])


@app.get("/")
def root():
    return {"message": "Smart WhatsApp AI CRM API online ✅"}