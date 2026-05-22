# Automated Structural Damage Assessment via Photo Severity Index (PSI)

An automated computer vision solution developed in Python to detect, segment, and categorize structural damage (such as cracks or surface anomalies on buildings) from image data. By leveraging adaptive thresholding and contour analysis, this tool calculates the total affected surface area, maps it to a **Photo Severity Index (PSI)**, and generates visual overlays for rapid engineering or structural inspection.

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
1.  **Image Ingestion:** Loads the source file into memory using OpenCV.
2.  **Color Space Optimization:** Converts BGR channels to Grayscale to simplify pixel intensity mapping.
3.  **Binarization:** Applies an inverse adaptive threshold to turn relevant surface damage structures into isolated binary objects.
4.  **Morphological Segmentation:** Detects external contours (`cv2.findContours`) and filters out minor noise where the contour area is less than or equal to 100 pixels.
5.  **Metrics Generation:** Aggregates valid damaged areas against total pixel dimensions to derive a pure percentage metric.
6.  **Classification:** Evaluates the index tier and logs total computational runtime.
7.  **Rendering:** Layers rectangular ROI bounding-boxes and blending masks over the original frame.

---

## 🛠️ Environment & Prerequisites

This workflow is optimized out-of-the-box for **Google Colab** to make use of cloud file-upload dialogs and inline image rendering patches (`cv2_imshow`).

### Core Dependencies
Ensure you have the following packages installed if running inside a cloud environment:
* Python 3.x
* OpenCV (`opencv-python`)
* NumPy

---

## 🚀 Getting Started

1.  Create a new notebook inside **Google Colab**.
2.  Create a file named `main.py` or paste the code into an empty cell.
3.  Execute the cell. A file picker button will appear under the console output.
    > 💡 **Tip:** Upload a clear, high-resolution JPEG or PNG image of the affected building facade for the most accurate assessment results.
4.  The notebook will render three distinct image arrays (Original, ROI bounding boxes, and Masked) followed by a comprehensive analytical breakdown report.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute this software for personal, academic, or commercial production pipelines.
