#!/bin/bash
pip install -r requirements.txt --break-system-packages --no-warn-script-location
python -m xmlrunner test_dynamic_controls.py -o ./test-reports

