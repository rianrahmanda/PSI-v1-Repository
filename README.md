# Automated Structural Damage Assessment via Photo Severity Index (PSI)

A Python computer vision tool that detects, segments, and categorizes structural damage (such as cracks or surface anomalies on buildings) in images. It uses adaptive thresholding and contour analysis to calculate the damaged surface area, maps it to a **Photo Severity Index (PSI)**, and draws visual overlays for structural inspection.

---

## 🚀 Installation & Running

You need **Python 3.10 or newer**. Run these commands inside the project folder.

**Windows (Command Prompt or PowerShell)**

```bat
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

**macOS / Linux**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

Open <http://localhost:8501> and upload an image of a building facade (JPEG, PNG, BMP, or WebP). Next time, run only the last line.

Need help with Python, Git, or errors? See the full guide for [Windows](docs/install-windows.md), [macOS](docs/install-macos.md), or [Linux](docs/install-linux.md).

---

## ⚙️ Key Features

* **Gaussian Adaptive Thresholding:** Dynamically isolates damaged textures or surface cracks under varying or uneven lighting conditions.
* **Contour-Based Segmentation:** Automatically extracts damaged patterns using OpenCV's external contour detection algorithms.
* **Noise Filtering:** Removes minor image artifacts, shadows, and background noise by discarding contours of 100 pixels or smaller.
* **Quantitative Scaling:** Computes the exact percentage of structural damage relative to the overall surface area.
* **5-Tier Severity Classification:** Categorizes structural conditions with a rubric that you can change in `SEVERITY_RUBRIC` (`core/psi.py`).
* **Dual-Mode Visualization:** Outputs an ROI (Region of Interest) bounding-box view alongside a semi-transparent red alpha-blend mask overlay.
* **Execution Profiling:** Tracks real-time script runtime to monitor computing efficiency.

---

## 📊 Damage Classification Rubric

The system evaluates the computed damage percentage and assigns a specific severity index based on the following framework:

| Damage Percentage | PSI Index | Damage Category | Color |
| :--- | :---: | :--- | :--- |
| ≤ 20% | 0 | Minimal damage | Green |
| > 20% – 40% | 1 | Light damage | Yellow |
| > 40% – 60% | 2 | Moderate damage | Orange |
| > 60% – 80% | 3 | Severe damage | Red |
| > 80% | 4 | Very severe damage | Dark red |

---

## 🧠 Algorithmic Workflow

1. **Image Ingestion:** Loads the uploaded file with Pillow and converts it to an RGB array.
2. **Color Space Optimization:** Converts the RGB channels to grayscale to simplify pixel intensity mapping.
3. **Binarization:** Applies an inverse adaptive threshold to turn relevant surface damage structures into isolated binary objects.
4. **Morphological Segmentation:** Detects external contours (`cv2.findContours`) and filters out minor noise where the contour area is less than or equal to 100 pixels.
5. **Metrics Generation:** Aggregates valid damaged areas against total pixel dimensions to derive a pure percentage metric.
6. **Classification:** Evaluates the index tier and logs total computational runtime.
7. **Rendering:** Layers rectangular ROI bounding-boxes and blending masks over the original frame.

---

## 📄 License

This project uses the **MIT License**. See the [LICENSE](LICENSE) file for details.
