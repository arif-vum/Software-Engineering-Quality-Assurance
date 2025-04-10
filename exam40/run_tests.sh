#!/bin/bash
# Jenkins test runner script

# Activate Python environment
source ./selenium_env/bin/activate

# Install requirements
pip install -r requirements.txt

# Run tests with headless Firefox
python3 -m unittest test_dynamic_controls.py




# Deactivate environment
deactivate


