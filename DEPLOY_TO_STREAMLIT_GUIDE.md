# 🚀 Deploying CreditFlow AI to Streamlit Community Cloud

This guide provides instructions to deploy the **CreditFlow AI Multi-Agent Credit Assessment & Loan Pre-Screening System** to **Streamlit Community Cloud (100% Free)**, **Docker**, or **Hugging Face Spaces**.

---

## ⚡ Architecture & Deployment Highlights

- **Pure Python 3.11+ Multi-Agent Pipeline:** Exactly 7 decoupled operational agents coordinating deterministically.
- **Dual Product Underwriting:** Independent **Personal Loan** and **Higher Education Loan** policies with zero cross-policy leakage.
- **Embedded Machine Learning:** Calibrated Scikit-Learn risk pipeline (`artifacts/credit_risk_model.joblib`).
- **Normalized SQLite Database:** Auto-initialized tables and audit logging (`data/loan_prescreening.db`).
- **Zero Paid API Requirements:** Pure deterministic rule execution, financial calculations, and local ML inference without requiring paid API keys.
- **Dual Cloud Entry Points:** Both `streamlit_app.py` and `app.py` are configured for instant cloud detection.

---

## 🌐 Method 1: Deploy to Streamlit Community Cloud (Recommended & Free)

Deploying to **[Streamlit Community Cloud](https://streamlit.io/cloud)** is free and takes under 2 minutes.

### Step 1: Upload Your Code to GitHub

#### Option A: Using the GitHub Web Interface (No Git Installed Required)
1. Go to [github.com/new](https://github.com/new) and sign in.
2. Enter a repository name (e.g. `creditflow-ai`), keep it **Public**, and click **Create repository**.
3. On the repository page, click **"uploading an existing file"**.
4. Drag and drop all the files from this project directory:
   - `app.py`
   - `streamlit_app.py`
   - `requirements.txt`
   - `packages.txt`
   - `.streamlit/`
   - `agents/`
   - `services/`
   - `models/`
   - `ui_pages/`
   - `ml/`
   - `config/`
   - `artifacts/`
   - `data/`
5. Click **Commit changes**.

#### Option B: Using Git Command Line (If Git is installed)
```bash
git init
git add .
git commit -m "Deploy CreditFlow AI Multi-Agent Pre-Screening System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/creditflow-ai.git
git push -u origin main
```

---

### Step 2: Connect Streamlit Community Cloud
1. Go to **[share.streamlit.io](https://share.streamlit.io)** and click **Sign in with GitHub**.
2. Click the blue **"Create app"** button.
3. Select **"I already have an app"**.
4. Configure the deployment settings:
   - **Repository:** `YOUR_USERNAME/creditflow-ai`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py` *(or `app.py`)*
   - **App URL (Optional):** Customize your free subdomain, e.g., `creditflow-ai.streamlit.app`
5. Click **Deploy!**

---

### Step 3: Deployment Verification
Streamlit Cloud will automatically:
1. Read `packages.txt` and install required Linux graphics/PDF libraries (`libgl1-mesa-glx`, `libglib2.0-0`, `curl`).
2. Read `requirements.txt` and install all Python dependencies.
3. Apply the theme settings from `.streamlit/config.toml` (Cobalt Blue `#2563EB`).
4. Launch the application!

Your app will be live at:
👉 **`https://YOUR-APP-NAME.streamlit.app`**

---

## 🔐 Built-in Demonstration Logins

Once deployed, you can log in to test any role using the **"⚡ 1-Click Demo Login"** buttons on the login screen:

| Role | Username | Password | Key Permissions |
| :--- | :--- | :--- | :--- |
| 👮 **Credit Officer** | `officer` | `password123` | Executive Dashboard, Underwriter Queue, Verification, Sandboxes |
| 🕵️ **Fraud Investigator** | `investigator` | `password123` | Fraud Queue, Tamper Inspection, Risk Flags |
| 🛡️ **Administrator** | `admin` | `password123` | Full Audit Logs, Responsible AI & Settings, Sandboxes |
| 👤 **Applicant (Borrower)** | `applicant` | `password123` | Submit Applications, Upload Documents, View Status |

---

## 💻 Method 2: Run Locally on Your Computer

### Prerequisites
- Python 3.11+
- Virtual Environment (recommended)

### Commands
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run automated test suite (52 tests across 7 test files)
python -m pytest tests/ -v

# 3. Launch the Streamlit application
streamlit run app.py
```
*(If `streamlit` is not recognized in your terminal, use `python -m streamlit run app.py`)*

Open your browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🐳 Method 3: Deploy with Docker or Hugging Face Spaces

This repository includes a production-ready [`Dockerfile`](file:///c:/Users/HP/Downloads/fintech%20app/Dockerfile):

### Building & Running with Docker Locally:
```bash
# 1. Build Docker image
docker build -t creditflow-ai .

# 2. Run container on port 8501
docker run -p 8501:8501 creditflow-ai
```
Open **[http://localhost:8501](http://localhost:8501)**.

### Deploying to Hugging Face Spaces:
1. Create a new Space on **[Hugging Face](https://huggingface.co/spaces)**.
2. Select **Streamlit** as the Space SDK.
3. Push or upload this repository to your Space.
4. Hugging Face Spaces will build the environment and launch the app automatically.

---

## ⚙️ Advanced Configuration (Streamlit Secrets)

If you wish to customize runtime environment variables on Streamlit Cloud, go to your app settings on Streamlit Cloud $\rightarrow$ **Settings** $\rightarrow$ **Secrets** $\rightarrow$ enter:

```toml
# Default Annual Interest Rate (%)
DEFAULT_ANNUAL_INTEREST_RATE = 12.0

# Max Permitted Debt-to-Income Ratio (DTI)
MAX_PERMITTED_DTI = 0.55

# Maximum Upload Size (MB)
MAX_FILE_SIZE_MB = 15

# Integration Toggles (Keep true for simulated academic sandbox)
SIMULATED_KYC_MODE = "true"
SIMULATED_BUREAU_MODE = "true"
SIMULATED_BANKING_MODE = "true"
SIMULATED_DISBURSEMENT_MODE = "true"
```
