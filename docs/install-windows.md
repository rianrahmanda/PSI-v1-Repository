# Install on Windows

[← Back to README](../README.md)

## 1. Install Python

1. Download **Python 3.10 or newer** from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer and tick **Add python.exe to PATH**.
3. Open **Command Prompt** and check the version:

```bat
py --version
```

## 2. Get the code

**With Git:**

```bat
git clone https://github.com/rianrahmanda/PSI-v1-Repository.git
cd PSI-v1-Repository
```

**Without Git:** on the GitHub page, click **Code → Download ZIP** and extract it. Open the extracted folder `PSI-v1-Repository-main` in File Explorer, type `cmd` in the address bar, and press `Enter`.

## 3. Install (one time)

```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

After activation, your prompt starts with `(.venv)`.

## 4. Run

```bat
.venv\Scripts\activate
streamlit run app.py
```

You only need to activate once per terminal window. If your prompt already shows `(.venv)`, skip the first line.

Open <http://localhost:8501> in your browser. Press `Ctrl+C` in the terminal to stop the app. Type `deactivate` to leave the environment.

Next time, open a terminal inside the project folder and run only step 4.

These commands work in Command Prompt and PowerShell.

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `'py' is not recognized` | Use `python` instead of `py`. If that also fails, install Python again and tick **Add python.exe to PATH**. |
| `'git' is not recognized` | Use the **Download ZIP** option in step 2. |
| PowerShell: `running scripts is disabled on this system` | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again. Or use Command Prompt. |
| `'streamlit' is not recognized` | The environment is not active. Run `.venv\Scripts\activate` first. |
| Port 8501 is busy | Add `--server.port 8502` to the run command. |
