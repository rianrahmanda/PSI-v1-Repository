# Automated Structural Damage Assessment via Photo Severity Index (PSI)

An automated computer vision solution developed in Python to detect, segment, and categorize structural damage (such as cracks or surface anomalies on buildings) from image data. By leveraging adaptive thresholding and contour analysis, this tool calculates the total affected surface area, maps it to a **Photo Severity Index (PSI)**, and generates visual overlays for rapid engineering or structural inspection.

---

## 🚀 Installation & Running

You need **Python 3.10 or newer** and **Git**. Check with `python --version` (on Windows you can also use `py --version`).

### Linux / macOS

```bash
git clone https://github.com/rianrahmanda/PSI-v1-Repository.git
cd PSI-v1-Repository
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

### Windows (Command Prompt)

```bat
git clone https://github.com/rianrahmanda/PSI-v1-Repository.git
cd PSI-v1-Repository
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

The same commands work in PowerShell. If `py` is not found, use `python` instead.

The install step runs once. Next time, only run the last line.

When the server starts, open <http://localhost:8501> in your browser. Press `Ctrl+C` in the terminal to stop it.

> 💡 **Tip:** Upload a clear, high-resolution JPEG or PNG image of the affected building facade for the most accurate assessment results. The app renders the Original, ROI bounding-box, and Masked views alongside the full analytical breakdown.

### Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `'python' is not recognized` (Windows) | Install Python from [python.org](https://www.python.org/downloads/) and tick **Add python.exe to PATH**, or use `py`. |
| `No module named venv` (Debian/Ubuntu) | `sudo apt install python3-venv` |
| Port 8501 is busy | Add `--server.port 8502` to the run command. |

### Developer commands (Linux / macOS, needs [`just`](https://github.com/casey/just))

The `justfile` uses `bash`, so these recipes do not run in Windows Command Prompt.

| Command | Purpose |
| :--- | :--- |
| `just install` | Create `.venv/` and install requirements plus `ruff` |
| `just dev` | Start the Streamlit dev server |
| `just test` | Run the unit test suite (`pytest`) |
| `just lint` | Lint with `ruff` |
| `just format` | Auto-format with `ruff` |

---

## ⚙️ Key Features

* **Gaussian Adaptive Thresholding:** Dynamically isolates damaged textures or surface cracks under varying or uneven lighting conditions.
* **Contour-Based Segmentation:** Automatically extracts damaged patterns using OpenCV's external contour detection algorithms.
* **Intelligent Noise Filtering:** Eliminates minor image artifacts, shadows, or background noise by filtering out contours smaller than 100 pixels.
* **Quantitative Scaling:** Computes the exact percentage of structural damage relative to the overall surface area.
* **5-Tier Severity Classification:** Automatically categorizes structural conditions based on a customizable assessment rubric.
* **Dual-Mode Visualization:** Outputs an ROI (Region of Interest) bounding-box view alongside a semi-transparent red alpha-blend mask overlay.
* **Execution Profiling:** Tracks real-time script runtime to monitor computing efficiency.

---

## 📊 Damage Classification Rubric

The system evaluates the computed damage percentage and assigns a specific severity index based on the following framework:

| Damage Percentage | PSI Index | Damage Category | Visual Indicator |
| :--- | :---: | :--- | :--- |
| <= 20% | 0 | Minimal damage | Green Box / Red Mask |
| 21% - 40% | 1 | Light damage | Green Box / Red Mask |
| 41% - 60% | 2 | Moderate damage | Green Box / Red Mask |
| 61% - 80% | 3 | Severe damage | Green Box / Red Mask |
| > 80% | 4 | Very severe damage | Green Box / Red Mask |

---

## 🧠 Algorithmic Workflow

1. **Image Ingestion:** Loads the source file into memory using OpenCV.
2. **Color Space Optimization:** Converts BGR channels to Grayscale to simplify pixel intensity mapping.
3. **Binarization:** Applies an inverse adaptive threshold to turn relevant surface damage structures into isolated binary objects.
4. **Morphological Segmentation:** Detects external contours (`cv2.findContours`) and filters out minor noise where the contour area is less than or equal to 100 pixels.
5. **Metrics Generation:** Aggregates valid damaged areas against total pixel dimensions to derive a pure percentage metric.
6. **Classification:** Evaluates the index tier and logs total computational runtime.
7. **Rendering:** Layers rectangular ROI bounding-boxes and blending masks over the original frame.

---

## 🛠️ Environment & Prerequisites

The project ships as a **Streamlit** web application. You upload an image through the browser and the app renders the analysis inline.

### Core Dependencies

* Python 3.10+
* [Streamlit](https://streamlit.io/) (`streamlit>=1.30`)
* OpenCV (`opencv-python-headless>=4.8`)
* NumPy (`numpy>=1.24`)
* Pillow (`pillow>=10.0`)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute this software for personal, academic, or commercial production pipelines.
