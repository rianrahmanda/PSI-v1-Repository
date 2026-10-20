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
.venv\Scripts\python -m pip install -r requirements.txt
```

## 4. Run

```bat
.venv\Scripts\python -m streamlit run app.py
```

Open <http://localhost:8501> in your browser. Press `Ctrl+C` in the terminal to stop the app.

Next time, open a terminal inside the project folder and run only step 4.

These commands also work in PowerShell.

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `'py' is not recognized` | Use `python` instead of `py`. If that also fails, install Python again and tick **Add python.exe to PATH**. |
| `'git' is not recognized` | Use the **Download ZIP** option in step 2. |
| Port 8501 is busy | Add `--server.port 8502` to the run command. |
