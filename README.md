
# 🚨 Incident Orchestrator 

## 📌 Description

Incident Orchestrator v2.0 is an AI-powered multi-agent system designed to analyze application error logs and generate precise remediation steps. The system leverages **Nanobot CLI** for orchestrating multiple intelligent agents in a secure and structured pipeline.

It performs deep Root Cause Analysis (RCA) and produces actionable fixes while defending against prompt injection and hallucinations.

---

## ⚙️ Features

* 🔍 **AI Root Cause Analysis (RCA)**

  * Uses Nanobot-powered agent to extract exact failure reasons
  * Ignores noise, comments, and misleading hints
  * Strict anti-hallucination logic

* 🛠️ **Automated Remediation Suggestions**

  * Step-by-step fixes based only on RCA output
  * Includes prevention strategies

* 🤖 **Multi-Agent Orchestration (Nanobot)**

  * Agent 1 → Root Cause Analysis
  * Agent 2 → Remediation Generator
  * Fully isolated and controlled execution

* 🔄 **Multi-LLM Fallback System**

  * OpenRouter → Gemini → Groq
  * Ensures reliability and availability

* 🔐 **JWT Authentication**

  * Secure API access using bearer tokens

* 🛡️ **Prompt Injection Protection**

  * Detects malicious or non-log inputs
  * Returns `INVALID_LOG_FORMAT` for unsafe content

* 🐳 **Dockerized Deployment**

  * Runs FastAPI + Streamlit using Supervisor
  * Easy deployment on AWS EC2

---

## 🏗️ Architecture

```
User (Streamlit UI)
        ↓
   FastAPI Backend (/analyze)
        ↓
   Nanobot CLI Orchestration
        ↓
  ┌───────────────────────┐
  │  Agent 1: RCA Agent   │
  └───────────────────────┘
        ↓
  ┌──────────────────────────┐
  │ Agent 2: Remediation     │
  └──────────────────────────┘
        ↓
     Response (UI)
```

---

## 🚀 Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Agent Framework:** Nanobot CLI
* **LLM Providers:** OpenRouter, Gemini, Groq
* **Deployment:** Docker + AWS EC2
* **Authentication:** JWT

---

## 📥 Input

* Raw error logs / stack traces
* JSON or plain text supported

---

## 📤 Output

* Root Cause Analysis (precise technical cause)
* Recommended Fixes (step-by-step actions)
* Prevention Insights

---

## 🔧 Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/incident-bot.git
cd incident-bot
```

### 2. Build Docker image

```
docker build -t incident-bot .
```

### 3. Run container

```
docker run -d -p 8000:8000 -p 8501:8501 incident-bot
```

---

## 🌐 Usage

* Streamlit UI → http://localhost:8501
* FastAPI Docs → http://localhost:8000/docs

---

## 🔐 Authentication

Provide a valid JWT token in the UI sidebar to access the analysis pipeline.

---

## ⚠️ Security Considerations

* Rejects non-log or suspicious inputs
* Prevents prompt injection attacks
* Avoids unsafe automated execution
* Ensures agent isolation via Nanobot

---

## 📌 Future Enhancements

* Kubernetes deployment
* Real-time log ingestion
* Alert integrations (Slack, Email)
* Observability dashboard

---

## 👩‍💻 Author

Built as an AI-driven incident analysis system leveraging Nanobot for reliable multi-agent orchestration.

---

## ⭐ Contributing

Pull requests are welcome. Please open an issue to discuss major changes.

---

## 📄 License

MIT License
