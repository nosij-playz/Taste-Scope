from flask import Flask, request, render_template, redirect, url_for, session
from tastescope import FoodClassifier, FoodInfo
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for session
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

classifier = FoodClassifier()
info = FoodInfo()

@app.route('/', methods=['GET', 'POST'])
def index():
    # Delete previously uploaded image if exists
    last_image = session.pop('uploaded_image', None)
    if last_image:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], last_image))
        except FileNotFoundError:
            pass

    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "No image uploaded", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Save image name to session
    session['uploaded_image'] = file.filename

    prediction = classifier.predict(file_path)
    info.set(prediction)

    return render_template('result.html',
                           prediction=prediction,
                           description=info.get_description(),
                           calories=info.get_calories(),
                           ingredients=info.get_ingredients(),
                           portion_size=info.get_portion_size(),
                           origin=info.get_origin(),
                           image_url=url_for('static', filename='uploads/' + file.filename))

if __name__ == '__main__':
    app.run(debug=True)
