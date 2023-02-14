#start.sh

#!/bin/bash
# This script starts the python webapp

#!/bin/bash

# activate virtual environment
source venv/bin/activate

# set environment variables (if any)
export FLASK_APP=app.py
export FLASK_ENV=development

# run the application
flask run --host=0.0.0.0
