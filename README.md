# Git Email Switch

This python program switches the current git email between two emails.

## Setup

Windows:

```Powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configure

Create a YAML file in the folder called `config.yml` with the two emails desired.

```YAML
- email1@example.com
- email2@example.com
```

## Run

```sh
python email_switch.py
```

For usage with Logitech G HUB macros, the batch file can be used. The batch file will only work if the repository is in the home folder.
