# Project Deep Dive: Ripe Strawberry Detection using YOLO

This project demonstrates a complete, end-to-end workflow for training a custom YOLO object detection model to identify and locate ripe strawberries in images, with potential applications in automated agriculture.

---

### Problem Statement & Goal
The primary goal was to build and train an efficient object detection model capable of locating ripe strawberries in images. This has practical applications in automated harvesting, agricultural yield estimation, and fruit quality assessment. The project aimed to deliver a high-performance model trained on a custom dataset.

### My Role
I was the sole developer for this project, responsible for the entire workflow, including data preprocessing, model selection and training, performance evaluation, and final model export.

### Architecture & Methodology
The end-to-end process was implemented in a Jupyter Notebook (`object-detection.ipynb`) using the Ultralytics YOLOv8 framework.

* **Data Preprocessing**: The initial dataset was provided as a single `annotations.xml` file. I developed a script to parse this XML, extract bounding box coordinates (`xtl`, `ytl`, `xbr`, `ybr`) , and convert them into the normalized YOLO format (`Xcent`, `Ycent`, `boxW`, `boxH`) required for training. The processed annotations, with a class label of `0` for all strawberries, were saved as individual `.txt` files for each image.
* **Data Splitting**: The dataset was randomly shuffled and split into training (25 images), validation (10 images), and test sets , which were then organized into the required directory structure (`train`, `valid`, `test`).
* **Model Training**: A pretrained **YOLOv11n** model from the `ultralytics` library was used as the base for fine-tuning. The model was trained for **100 epochs** on the custom strawberry dataset using a GPU, with an input image size of 640x640.
* **Model Evaluation**: After training, the model's performance was measured on the validation set using standard object detection metrics, specifically **mAP50** (mean Average Precision at IoU > 0.5) and **mAP50-95** (averaged over multiple IoU thresholds).
* **Prediction & Export**: The final trained model was used for inference on test images to visually confirm its performance. For deployment, the model was exported to the **ONNX** format with dynamic input shapes, ensuring portability across various platforms.

---

### Key Technical Challenges & Solutions
1.  **Challenge: Incompatible Annotation Format**
    * **Problem**: The provided annotations were in a single XML file, which is not directly compatible with the YOLO training pipeline that requires one `.txt` file per image.
    * **Solution**: I implemented a data preprocessing workflow using pandas to parse the XML file , restructure the data, and systematically convert each bounding box to the required normalized YOLO format. The script then generated the corresponding `.txt` label file for every image in the dataset.

2.  **Challenge: Ensuring Model Portability for Deployment**
    * **Problem**: A trained model in a proprietary framework format can be difficult to deploy in different environments.
    * **Solution**: After validating the model, I exported the final weights to the ONNX (Open Neural Network Exchange) format. This creates a standardized, framework-agnostic model that is highly portable and can be deployed on a wide range of hardware and software platforms.

---

### Technologies & Tools Used
* **Framework & Libraries:** Ultralytics YOLOv8, Python, pandas 
* **Development Environment:** Jupyter Notebook 
* **Data Formats:** XML (source), YOLO `.txt` (training), ONNX (export) 

---

### Results & Performance
The model was successfully trained, and its performance on the validation set indicates a high level of accuracy for the detection task.

| Metric   | Value |
| :------- | :---- |
| mAP50    | 0.968 |
| mAP50-95 | 0.779 |

*Table data sourced from *

These strong results confirm the model's effectiveness in accurately identifying ripe strawberries, making it suitable for its intended real-world applications.