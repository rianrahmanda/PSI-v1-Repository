# Install on Linux

[← Back to README](../README.md)

## 1. Install Python

Check the version. You need **3.10 or newer**:

```bash
python3 --version
```

On Debian or Ubuntu, also install the `venv` module:

```bash
sudo apt install python3-venv
```

## 2. Get the code

```bash
git clone https://github.com/rianrahmanda/PSI-v1-Repository.git
cd PSI-v1-Repository
```

No Git? On the GitHub page, click **Code → Download ZIP**, extract it, and `cd` into `PSI-v1-Repository-main`.

## 3. Install (one time)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After activation, your prompt starts with `(.venv)`.

## 4. Run

```bash
source .venv/bin/activate
streamlit run app.py
```

You only need to activate once per terminal window. If your prompt already shows `(.venv)`, skip the first line.

Open <http://localhost:8501> in your browser. Press `Ctrl+C` in the terminal to stop the app. Type `deactivate` to leave the environment.

Next time, `cd` into the project folder and run only step 4.

## Optional: shortcuts with `just`

If you have [`just`](https://github.com/casey/just), these commands do the same work with less typing.

| Command | Purpose |
| :--- | :--- |
| `just install` | Create `.venv/` and install requirements plus `ruff` |
| `just dev` | Start the Streamlit dev server |
| `just test` | Run the unit test suite (`pytest`) |
| `just lint` | Lint with `ruff` |
| `just format` | Auto-format with `ruff` |

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `No module named venv` or `ensurepip is not available` | `sudo apt install python3-venv` (Debian/Ubuntu) |
| `streamlit: command not found` | The environment is not active. Run `source .venv/bin/activate` first. |
| Port 8501 is busy | Add `--server.port 8502` to the run command. |
