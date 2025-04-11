#!/bin/bash
# Jenkins test runner script

# Activate Python environment
source ./selenium_env/bin/activate
alias pip="./selenium_env/bin/pip"
alias python="./selenium_env/bin/python"

# Install requirements
pip install -r requirements.txt

# Run tests with headless Firefox
python -m unittest test_dynamic_controls.py




# Deactivate environment
deactivate


