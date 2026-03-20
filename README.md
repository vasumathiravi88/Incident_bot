# 🚨 Incident Knowledge Assistant API

## 📌 Description

Incident Knowledge Assistant v1.0 is a **FastAPI-based service** designed to analyze application error logs and provide precise Root Cause Analysis (RCA) along with actionable remediation steps.  

It leverages a **unified Nanobot agent** (RCA + remediation combined) and supports **tiered LLM providers** (OpenRouter, Gemini, Groq). Security features include **prompt injection protection, hallucination mitigation, log sanitization, and JWT authentication**.  

Logs can be sent directly as **JSON payloads**, making integration with Postman or other API clients simple.

---

## ⚙️ Features

* 🔍 **AI Root Cause Analysis**
  * Analyzes technical error logs only
  * Returns precise root cause and step-by-step fixes
  * Anti-hallucination logic ensures outputs are factual
  * Rejects logs with suspicious patterns

* 🤖 **Unified Nanobot Agent (RCA + Remediation)**
  * Single CLI agent performs both analysis and remediation
  * Cleans noisy outputs automatically
  * Masks sensitive data (`password`, `token`, `apikey`)
  * Does not execute unsafe commands; analysis only

* 🔄 **Multi-LLM Fallback System**
  * **Tier 1:** OpenRouter  
  * **Tier 2:** Gemini  
  * **Tier 3:** Groq  
  * Ensures analysis completes even if one provider fails

* 🔐 **JWT Authentication**
  * Secure API access via `Bearer` tokens
  * Demo route `/generate_token` issues a 10-day token

* 🛡️ **Security & Input Validation**
  * Rejects non-log, HTML/script, or malicious content
  * Sanitizes dangerous instructions (`reveal secrets`, `ignore previous instructions`, etc.)
  * Returns standardized response for unsafe inputs

* 🐳 **Docker-Ready**
  * Easy deployment on AWS EC2 or local environment
  * Includes FastAPI backend with CORS support

* 🌐 **Postman-Friendly JSON Input**
  * Logs can be sent directly in `"error_log"` field as JSON
  * No manual escaping required

---

## 🏗️ Architecture

```text
User (Streamlit UI / API Client)
        ↓
    FastAPI Backend (/analyze)
        ↓
Unified Nanobot Agent (RCA + Remediation)
        ↓
   JSON Response (resolution)