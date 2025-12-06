# 🤖 Smart WhatsApp AI CRM — Intelligent Virtual Sales Assistant (FastAPI + Gemini + PostgreSQL)

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.123-009688?style=flat&logo=fastapi)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange?style=flat&logo=google)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat&logo=sqlalchemy)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=flat&logo=postgresql)

Smart WhatsApp AI CRM is a **production-grade Minimum Viable Product (MVP)** designed to automate **customer acquisition, real-time support, and intelligent lead qualification** through the integration of **WhatsApp Webhooks, FastAPI, Google Gemini Generative AI, and PostgreSQL (Supabase)**. The system operates as an **AI-powered virtual sales assistant**, capable of receiving WhatsApp messages automatically, understanding user intent using large language models, guiding conversations with a commercial focus, extracting structured business data, and persisting complete conversation history asynchronously in a relational database. This project follows **enterprise backend engineering principles, clean architecture, and scalable SaaS-ready design**.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Key Features  
Real-time WhatsApp Webhook processing, strict payload validation using Pydantic, AI-driven conversational engine powered by Gemini 2.5 Flash, automatic lead qualification and data extraction (name, service interest, intent), asynchronous PostgreSQL persistence with SQLAlchemy 2.0, conversation history tracking, secure Webhook verification via token, API health monitoring endpoint, fully decoupled service-oriented architecture, and automatic OpenAPI/Swagger documentation.

The AI operates as a **virtual sales representative**, maintaining conversation context, enforcing commercial guardrails via system prompts, avoiding topic drift, guiding prospects through the sales funnel, and generating structured insights for CRM and analytics.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Project Structure (Real Implementation)

```plaintext
SMART-WHATSAPP-AI-CRM
├── app
│   ├── core
│   │   ├── config.py        # Global environment configuration
│   │   └── security.py      # Security helpers and validation utilities
│   ├── db
│   │   ├── base.py          # SQLAlchemy declarative base
│   │   ├── session.py       # Asynchronous database session and engine
│   │   └── init_db.py       # Automatic database initialization
│   ├── models
│   │   ├── lead.py          # Lead relational model
│   │   ├── message.py       # Message history model
│   │   └── user.py          # User model (SaaS-ready)
│   ├── routes
│   │   ├── health.py        # API health endpoint
│   │   ├── leads.py         # Lead management endpoints
│   │   └── whatsapp.py     # Official WhatsApp Webhook integration
│   ├── schemas
│   │   ├── whatsapp.py     # Pydantic schemas for WhatsApp payloads
│   │   └── __init__.py
│   ├── services
│   │   ├── ai_service.py   # Google Gemini AI orchestration layer
│   │   └── __init__.py
│   └── main.py             # FastAPI application entry point
├── venv
├── .env                    # Environment variables (Git ignored)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 🎥 Live Demo (Swagger Test)

This demo demonstrates the **real-time execution of the WhatsApp Webhook endpoint** using the FastAPI interactive documentation (Swagger UI). The test simulates an inbound WhatsApp message, triggers the AI processing pipeline, updates the lead in the database, and returns an AI-generated response.

**Demo Steps:**
1. Open the interactive API documentation at `http://localhost:8000/docs`
2. Select the endpoint `POST /whatsapp/webhook`
3. Insert a sample WhatsApp payload in JSON format
4. Click **Execute**
5. Observe the `200 OK` response and the AI-generated reply in real time

**What this demo proves:**
- WhatsApp Webhook integration is functional
- Payload validation via Pydantic is working correctly
- Gemini AI is properly orchestrated
- Lead creation and update flow is operational
- Asynchronous PostgreSQL persistence is active
- End-to-end request/response pipeline is stable

*(A recorded GIF/video of this execution is attached below to demonstrate the system running in real time.)*

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">


## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | FastAPI, Uvicorn | High-performance asynchronous API |
| **Generative AI** | Google Gemini API (gemini-2.5-flash) | Natural language understanding and lead qualification |
| **Database / ORM** | PostgreSQL (Supabase), SQLAlchemy 2.0 | Asynchronous relational persistence |
| **Tooling & Security** | Pydantic, python-dotenv | Data validation and secure configuration loading |

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 🚀 Setup and Installation Guide

### Environment Setup  
Create and activate a virtual environment:

Bash  
python -m venv venv  
# Activate (Windows PowerShell)  
.\venv\Scripts\Activate.ps1

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Install Dependencies  
Install all core dependencies using the clean requirements.txt:

Bash  
pip install -r requirements.txt 

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Configuration (.env File)  
Create a file named `.env` in the project root and populate it with your confidential keys:

# Gemini API Key  
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

# Supabase / PostgreSQL Connection String (SQLAlchemy Async Format)  
SUPABASE_URL="postgresql+asyncpg://[USER]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]"

# WhatsApp Webhook Verification Token (Meta/Facebook)  
VERIFY_TOKEN="YOUR_WHATSAPP_VERIFY_TOKEN"

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Running the API  
Start the application server with Uvicorn:

Bash  
uvicorn app.main:app --reload  

After startup, the API will be available at:  
http://localhost:8000  
Interactive documentation (Swagger UI):  
http://localhost:8000/docs

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;"> 

### System Workflow  
A user sends a message via WhatsApp → Meta triggers the Webhook → the API validates the payload → data is routed to the AI service → Gemini generates the response using a sales-focused system prompt → the response is returned to WhatsApp → all messages and lead data are persisted asynchronously in PostgreSQL → the lead is automatically created or updated in the CRM.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Business Use Cases  
This solution is suitable for sales automation in clinics, beauty salons, real estate agencies, e-commerce platforms, service companies, customer support centers, and any organization that relies on WhatsApp as a primary communication channel.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

### Professional Scope  
This project demonstrates production-ready expertise in **Backend Engineering, AI Automation, API Integration, Cloud Databases, and SaaS Architecture**, making it highly suitable for technical recruiter evaluation.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

Author: Neusa Magalhães  
Role: AI Automation Engineer | Backend Developer | CRM & API Integrations  
Project Status: Functional MVP — Production Ready

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this software for educational and commercial purposes, provided that the original copyright and license notice are included.

<hr style="border: 0.5px solid #e5e5e5; margin: 20px 0;">

<p align="left">
  <a href="https://github.com/NeusaM21">
    <img src="https://img.shields.io/badge/⬅️-Voltar%20para%20o%20portfólio%20principal-blue?style=for-the-badge"/>
  </a>
</p>


