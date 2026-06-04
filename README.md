🌱 Plant Disease Prediction Using Deep Learning

📌 Project Overview
Plant Disease Prediction is a Deep Learning-based web application that identifies diseases in plant leaves from uploaded images. The system uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset to classify plant diseases and provide predictions through a user-friendly Flask web interface.
This project helps farmers, researchers, and agriculture enthusiasts detect plant diseases quickly and accurately, enabling timely treatment and reducing crop loss.

<img width="834" height="703" alt="Screenshot 2026-06-04 200533" src="https://github.com/user-attachments/assets/039d015d-cfff-4f1c-ad26-3e5528296d06" />


🎯 Objectives
Detect plant diseases from leaf images.
Train a CNN model using the PlantVillage dataset.
Build a web application using Flask.
Provide disease prediction along with confidence scores.
Create an easy-to-use interface for image upload and prediction.

🛠️ Technologies Used
Python
TensorFlow / Keras
Flask
HTML
CSS
NumPy
Pillow (PIL)

📂 Dataset
Dataset Used: PlantVillage Dataset
The dataset contains images of healthy and diseased plant leaves belonging to multiple crop categories.

Dataset Structure
dataset/
└── PlantVillage/
    ├── Apple___Apple_scab
    ├── Apple___Black_rot
    ├── Apple___healthy
    ├── Tomato___Early_blight
    ├── Tomato___Late_blight
    └── ...

🧠 Model Architecture
The CNN model consists of:
Convolution Layer (32 Filters)
Max Pooling Layer
Convolution Layer (64 Filters)
Max Pooling Layer
Flatten Layer
Dense Layer (128 Neurons)
Dropout Layer
Output Layer (Softmax)

📁 Project Structure
Plant Disease Prediction/
│
├── dataset/
│   └── PlantVillage/
│
├── train/
├── test/
│
├── static/
│
├── templates/
│   └── index.html
│
├── create_balanced_dataset.py
├── train_model.py
├── app.py
├── plant_disease_model.h5
├── labels.txt
└── README.md

⚙️ Installation
Clone the Repository
git clone <repository-url>
cd Plant-Disease-Prediction
Create Virtual Environment
python -m venv .venv
Activate Virtual Environment

Windows:
.venv\Scripts\activate
Install Dependencies
pip install tensorflow flask numpy pillow

🚀 How to Run
Step 1: Create Balanced Dataset
python create_balanced_dataset.py
Step 2: Train the Model
python train_model.py

This generates:

plant_disease_model.h5
labels.txt

Step 3: Run Flask Application
python app.py
Step 4: Open Browser
http://127.0.0.1:5000
Step 5: Upload Leaf Image
Select a plant leaf image.
Click Predict.
View disease prediction and confidence score.

📊 Features
Image-based plant disease detection
Deep Learning CNN model
Flask web application
Disease prediction with confidence score
Simple and responsive user interface
Fast image processing

🔮 Future Enhancements
Increase dataset size for better accuracy.
Use transfer learning models such as ResNet50 and MobileNetV2.
Deploy on cloud platforms.
Add treatment and prevention recommendations.
Support real-time mobile image capture.

📈 Results

The model is trained on a balanced subset of the PlantVillage dataset and can classify plant diseases from uploaded leaf images through a Flask-based web interface.

👩‍💻 Author

Kaviya S

Machine Learning & Deep Learning Enthusiast

📝 License

This project is developed for educational and research purposes.
