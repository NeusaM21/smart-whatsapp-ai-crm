<p align="left">
  <a href="#smart-whatsapp-ai-crm--assistente-virtual-inteligente-de-vendas-fastapi--gemini--postgresql">
    <img src="https://img.shields.io/badge/🇧🇷-Versão%20em%20Português-green?style=for-the-badge"/>
  </a>
</p>

# 🤖 Smart WhatsApp AI CRM — Assistente Virtual Inteligente de Vendas (FastAPI + Gemini + PostgreSQL)

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.123-009688?style=flat&logo=fastapi)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange?style=flat&logo=google)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat&logo=sqlalchemy)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=flat&logo=postgresql)

Smart WhatsApp AI CRM é um **Produto Mínimo Viável (MVP) em nível de produção** desenvolvido para automatizar a **captação de clientes, atendimento em tempo real e qualificação inteligente de leads** por meio da integração entre **Webhooks do WhatsApp, FastAPI, Inteligência Artificial Generativa do Google Gemini e PostgreSQL (Supabase)**. O sistema atua como um **assistente virtual de vendas com IA**, capaz de receber mensagens automaticamente, compreender a intenção do usuário por meio de modelos de linguagem, conduzir conversas com foco comercial, extrair dados estruturados do cliente e persistir todo o histórico de conversas de forma assíncrona em um banco de dados relacional. Este projeto segue **princípios de engenharia backend corporativa, arquitetura limpa e design escalável pronto para SaaS**.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Principais Funcionalidades
Processamento de Webhook do WhatsApp em tempo real, validação rigorosa de payloads com Pydantic, motor conversacional orientado por IA com Gemini 2.5 Flash, qualificação automática de leads e extração de dados (nome, interesse e intenção), persistência assíncrona em PostgreSQL com SQLAlchemy 2.0, registro completo do histórico de conversas, verificação segura do Webhook por token, endpoint de saúde da API, arquitetura totalmente desacoplada por camadas e documentação automática via OpenAPI/Swagger.

A IA atua como uma **vendedora virtual**, mantendo o contexto da conversa, aplicando regras comerciais por meio de prompts de sistema, evitando desvios de assunto, conduzindo o cliente pelo funil de vendas e gerando dados estruturados para CRM e análises estratégicas.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Estrutura do Projeto (Implementação Real)

```plaintext
SMART-WHATSAPP-AI-CRM
├── app
│   ├── core
│   │   ├── config.py        # Configuração global de ambiente
│   │   └── security.py      # Utilitários de segurança e validação
│   ├── db
│   │   ├── base.py          # Base declarativa do SQLAlchemy
│   │   ├── session.py       # Sessão e engine assíncronos do banco
│   │   └── init_db.py       # Inicialização automática do banco
│   ├── models
│   │   ├── lead.py          # Modelo relacional de Lead
│   │   ├── message.py       # Modelo de histórico de mensagens
│   │   └── user.py          # Modelo de usuários (SaaS-ready)
│   ├── routes
│   │   ├── health.py        # Endpoint de saúde da API
│   │   ├── leads.py         # Endpoints de gerenciamento de leads
│   │   └── whatsapp.py     # Integração oficial com Webhook do WhatsApp
│   ├── schemas
│   │   ├── whatsapp.py     # Schemas Pydantic para payloads do WhatsApp
│   │   └── __init__.py
│   ├── services
│   │   ├── ai_service.py   # Camada de orquestração da IA Gemini
│   │   └── __init__.py
│   └── main.py             # Ponto de entrada da aplicação FastAPI
├── venv
├── .env                    # Variáveis de ambiente (ignoradas pelo Git)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 🎥 Demonstração ao Vivo (Teste via Swagger)

Esta demonstração apresenta a **execução em tempo real do endpoint de Webhook do WhatsApp** utilizando a documentação interativa do FastAPI (Swagger UI). O teste simula uma mensagem recebida pelo WhatsApp, aciona o pipeline de processamento com IA, atualiza o lead no banco de dados e retorna uma resposta gerada pela IA.

**Etapas da Demo:**
1. Acesse a documentação interativa em `http://localhost:8000/docs`
2. Selecione o endpoint `POST /whatsapp/webhook`
3. Insira um payload de exemplo em formato JSON
4. Clique em **Execute**
5. Observe o retorno `200 OK` e a resposta gerada pela IA

**O que esta demo comprova:**
- Integração com Webhook do WhatsApp funcional
- Validação de payload com Pydantic funcionando corretamente
- Orquestração da IA Gemini ativa
- Fluxo de criação e atualização de leads em operação
- Persistência assíncrona em PostgreSQL ativa
- Pipeline ponta-a-ponta estável

*(Um GIF ou vídeo gravado desta execução pode ser adicionado abaixo para demonstrar o sistema funcionando em tempo real.)*

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Finalidade |
| :--- | :--- | :--- |
| **Framework Backend** | FastAPI, Uvicorn | API assíncrona de alta performance |
| **IA Generativa** | Google Gemini API (gemini-2.5-flash) | Compreensão de linguagem e qualificação de leads |
| **Banco de Dados / ORM** | PostgreSQL (Supabase), SQLAlchemy 2.0 | Persistência relacional assíncrona |
| **Validação & Segurança** | Pydantic, python-dotenv | Validação de dados e carregamento seguro de variáveis |

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 🚀 Guia de Instalação e Execução

### Configuração do Ambiente
Crie e ative um ambiente virtual:

**Bash**
```bash
python -m venv venv 

# Ativação no Windows (PowerShell)  
.\venv\Scripts\Activate.ps1
```

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Instalação das Dependências  
Instale todas as dependências do projeto:

Bash  
pip install -r requirements.txt

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

#### Configuração do Arquivo .env
Crie um arquivo `.env` na raiz do projeto e insira suas chaves:

**Chave da API Gemini**
```env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

**String de Conexão Supabase / PostgreSQL (Formato Assíncrono do SQLAlchemy)**
```env
SUPABASE_URL="postgresql+asyncpg://[USER]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]"

**Token de Verificação do Webhook do WhatsApp (Meta/Facebook)
VERIFY_TOKEN="YOUR_WHATSAPP_VERIFY_TOKEN"
```
<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Execução da API

Inicie o servidor da aplicação com o Uvicorn:

Bash  
uvicorn app.main:app --reload  

Após iniciar, a API estará disponível em:  
http://localhost:8000  

Documentação interativa (Swagger UI):  
http://localhost:8000/docs  

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Fluxo de Funcionamento do Sistema
O usuário envia uma mensagem via WhatsApp → a Meta aciona o Webhook → a API valida o payload → os dados são enviados à IA → o Gemini gera a resposta → a resposta retorna ao WhatsApp → todas as mensagens e dados do lead são persistidos em PostgreSQL → o lead é criado ou atualizado automaticamente no CRM.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Casos de Uso de Negócio
Esta solução é ideal para automação de vendas em clínicas, salões de beleza, imobiliárias, plataformas de e-commerce, empresas de serviços, centrais de atendimento e qualquer organização que utilize o WhatsApp como canal principal de comunicação.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Escopo Profissional
Este projeto demonstra domínio prático em Engenharia Backend, Automação com IA, Integração de APIs, Bancos de Dados em Nuvem e Arquitetura SaaS, sendo altamente indicado para avaliação por recrutadores técnicos.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

**Autor:** Neusa Magalhães  
**Cargo:** AI Automation Engineer | Backend Developer | CRM & API Integrations  
**Email:** [contact.neusam21@gmail.com](mailto:contact.neusam21@gmail.com)  
**LinkedIn:** [https://www.linkedin.com/in/neusam21](https://www.linkedin.com/in/neusam21)  
**Status do Projeto:** MVP Funcional — Pronto para Produção  

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.  
Consulte o arquivo oficial:  
👉 [LICENSE](LICENSE)

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

<p align="left">
  <a href="https://github.com/NeusaM21">
    <img src="https://img.shields.io/badge/⬅️-Voltar%20para%20o%20portfólio%20principal-blue?style=for-the-badge"/>
  </a>
</p>


