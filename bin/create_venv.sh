echo "Creating the virtual enviroment"
declare VENV_DIR=$(pwd)/.venv
if ! [ -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi

echo "Activating the enviroment"
source $VENV_DIR/bin/activate

echo "Upgrading pip"
pip install --upgrade pip

FILE=requirements.txt
if test -f "$FILE"; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "No requirements file found, installing code formatting packages"
    pip install ruff interrogate nbqa pre-commit ipykernel
    pip freeze > requirements.txt
fi

PRE_COMMIT=.pre-commit-config.yaml
if test -f "$PRE_COMMIT"; then
    echo "Installing the hooks"
    pre-commit install
else
    echo "No .pre-commit-config.yaml file found, finish"
fi