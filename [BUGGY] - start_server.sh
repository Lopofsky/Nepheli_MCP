#!/bin/zsh
set -e  # Exit on error

DIR_NAME="${HOME}/claude_playground/rms_mcp"

# Check and change to directory
if [[ ! -d "${DIR_NAME}" ]]; then
    echo "Directory ${DIR_NAME} not found!" >&2
    exit 1
fi
cd "${DIR_NAME}" || exit 1

# Check and activate virtual environment
if [[ ! -f .venv/bin/activate ]]; then
    echo "Virtual environment not found!" >&2
    exit 1
fi
source .venv/bin/activate

uv pip install .

# Run the application
python3 src/rms_mcp/main.py
