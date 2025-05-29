
# 🍽️ Taste Scope

**Taste Scope** is a food image recognition app powered by deep learning. It identifies dishes from images and provides rich details including ingredients, calories, origin, and more.

---

## 📂 Project Structure

### `module/`
This folder contains the **trained deep learning model** and supporting files.  
It can be used as a standalone Python module.

- `main.py` – Sample usage of the model  
- `tastescope.py` – FoodClassifier and FoodInfo classes  
- `best_food101_resnet50.pth` – Pretrained ResNet-50 model on Food101  
- `class_names.json` – Food category labels  
- `food_info.json` – Descriptive data for each food class  

### `Taste Scope/`
This is the **Flask web app** for uploading and classifying food images.

- `app.py` – Main Flask application  
- `static/` – CSS, JS, and image preview assets  
- `templates/` – HTML pages (`index.html`, `result.html`)  
- `uploads/` – Temporary upload folder  
- `tastescope.py`, `best_food101_resnet50.pth`, `class_names.json`, `food_info.json` – Required model files (duplicated here for the app)

---

## 🚀 How to Run

### 📌 Prerequisites
- Python 3.7+
- PyTorch
- Flask
- Other dependencies listed in `requirements.txt` (create if needed)

### 🧪 Run the module manually (for testing model):

```bash
cd module
python main.py
```

### 🌐 Run the Flask Web App:

```bash
cd "Taste Scope"
python app.py
```

Then open your browser at `http://127.0.0.1:5000/`

---

## 🖼 Features

- Upload any food image
- Predict food name using ResNet-50
- Get:
  - 📝 Description  
  - 🥘 Ingredients  
  - 🔥 Calories  
  - 🍴 Portion Size  
  - 🌍 Origin

---

## 📬 Contact

For more information or to reach the developer:  
➡️ [Contact Me](https://myporfolio-1o1h.onrender.com/contact)

---

## 📄 License

This project is open-source. Feel free to use and modify it for educational or non-commercial purposes.
