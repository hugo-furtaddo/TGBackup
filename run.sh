# Get all sys args after file name
args=("$@")

source "$(dirname "$0")/venv/bin/activate"

# Run src/main.py with sys args
python "$(dirname "$0")/src/main.py" "$@"