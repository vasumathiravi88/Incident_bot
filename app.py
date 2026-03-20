import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="Incident Bot Toolkit", page_icon="💻", layout="wide")

# Vibrant Light Pink & Vibrant Blue Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

/* Apply modern typography */
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif !important;
}

/* General app background - Vibrant Gradient (Pink to Sky Blue) */
.stApp {
    background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
    background-attachment: fixed;
}

/* Make headers deeply colorful */
h1 {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    color: transparent;
    font-weight: 800 !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

h2, h3, h4 {
    color: #4a5568 !important;
    font-weight: 600 !important;
}

p, span, div {
    color: #2d3748 !important;
}

/* Agent Output Boxes - Bright White Glassmorphism */
div[data-testid="stInfo"] {
    background: rgba(255, 255, 255, 0.85);
    border-left: 6px solid #4299e1; /* Vibrant Blue border */
    border-radius: 12px;
    padding: 20px;
    font-size: 16px;
    color: #2b6cb0 !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

div[data-testid="stSuccess"] {
    background: rgba(255, 255, 255, 0.85);
    border-left: 6px solid #ed64a6; /* Vibrant Pink border */
    border-radius: 12px;
    padding: 20px;
    font-size: 16px;
    color: #b83280 !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

/* Inputs styling */
.stTextArea textarea {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #1a202c !important;
    border: 2px solid #cbd5e0 !important;
    border-radius: 10px !important;
    font-weight: 500;
}
.stTextArea textarea:focus {
    border-color: #a6c1ee !important;
    box-shadow: 0 0 0 1px #a6c1ee !important;
}

.stTextInput input {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #1a202c !important;
    border: 2px solid #cbd5e0 !important;
    border-radius: 10px !important;
    font-weight: 500;
}

/* Base button styling - Vibrant Pink/Purple Gradient */
button[kind="primary"] {
    background: linear-gradient(90deg, #b8c6db 0%, #f5f7fa 100%) !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08) !important;
    transition: all 0.2s ease !important;
    border-radius: 10px !important;
}
button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08) !important;
}

/* Sidebar styling - Light Glassmorphism */
div[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.6) !important;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

st.title("Incident Orchestrator v2.0")
st.markdown("Automated Multi-Agent Issue Resolution Pipeline")

# Initialize session state for auth token
if "auth_token" not in st.session_state:
    st.session_state["auth_token"] = None

# Sidebar Authentication
with st.sidebar:
    st.header("🔑 Auth Module")
    if not st.session_state["auth_token"]:
        st.markdown("**JWT Bearer Token Required**")
        token_input = st.text_input("Insert Signed JWT Token:", type="password")
        if st.button("Authenticate", type="primary"):
            if token_input:
                st.session_state["auth_token"] = token_input
                st.success("Token Loaded.")
                st.rerun()
            else:
                st.warning("Please provide a token.")
    else:
        st.success("Status: VERIFIED")
        if st.button("Drop Token", type="primary"):
            st.session_state["auth_token"] = None
            st.rerun()

st.subheader("Input Pipeline")
error_log = st.text_area("Paste Raw Stacktrace or Error Log here:", height=250)

if st.button("Execute Pipeline", type="primary"):
    if not st.session_state["auth_token"]:
        st.error("Unauthorized. Please provide your Bearer Token in the Sidebar.")
    elif not error_log.strip():
        st.warning("Payload Empty. Input required.")
    else:
        with st.spinner("INITIATING MULTI-AGENT SUBROUTINE..."):
            try:
                headers = {"Authorization": f"Bearer {st.session_state['auth_token']}"}
                # Use environment variable for backend URL in production, fallback to localhost
                BACKEND_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")
                payload = {"error_log": error_log}
                response = requests.post(f"{BACKEND_URL}/analyze", json=payload, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("**PROCESS: SUCCESS**")
                    
                    st.markdown("### 💡 Resolution")
                    with st.container():
                        st.success(data.get("resolution", "No resolution data provided in the response."))
                    
                    if data.get("errors_ignored"):
                        with st.expander("Fallback Pipeline Logs (Ignored Failures)"):
                            for err in data["errors_ignored"]:
                                st.error(err)
                                
                elif response.status_code == 401:
                    st.error("Token Invalid or Expired. Please Check your JWT.")
                else:
                    st.error(f"Execution Error: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Connection Refused. Verify API Backend Status is running on port 8000.")
