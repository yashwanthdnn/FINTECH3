"""
CreditFlow AI — Streamlit Cloud Production Deployment Entry Point
Automatically configures paths and executes the main application (app.py).
"""

import sys
import os
import runpy
from pathlib import Path

# Ensure root directory is at the top of sys.path for relative imports on cloud hosts
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Ensure required persistent storage directories exist
(ROOT_DIR / "data").mkdir(parents=True, exist_ok=True)
(ROOT_DIR / "artifacts").mkdir(parents=True, exist_ok=True)
(ROOT_DIR / "uploads").mkdir(parents=True, exist_ok=True)

# Run app.py in the main namespace
app_path = ROOT_DIR / "app.py"
runpy.run_path(str(app_path), run_name="__main__")
