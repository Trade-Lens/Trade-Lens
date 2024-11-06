# Instructions

> [!IMPORTANT]
> Before installing any packages be sure you are in the virtual environment.

### Enter the virtual environment
```bash
source venv/bin/activate
```
### Exit the virtual environment

```bash
deactivate
```

> [!NOTE]
> How to install the required packages and new packages.

1) When running the project for the first time, run:

```bash
pip install -r requirements.txt
```
2) When installing new dependencies, run:
```bash
pip install package_name
pip freeze >> requirements.txt
```
