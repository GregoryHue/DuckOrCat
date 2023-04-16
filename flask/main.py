from curses import flash
from flask import Flask, render_template, redirect, request
from keras.models import load_model
from werkzeug.utils import secure_filename
from PIL import Image
import numpy
import os

UPLOAD_FOLDER = os.path.join('static','media')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

m = load_model('model.h5')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def submit():
    return render_template('submit.html')


@app.route('/response', methods=['POST'])
def response():
    if request.method == "POST":
        image = request.files['image']
        if image.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            path_image = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path_image)
            image = Image.open(path_image)
            image = image.resize((128, 128))
            image = numpy.expand_dims(image, axis=0)
            image = numpy.array(image)
            image = image/255
            pred = m.predict([image])[0]
            cat_prob = round(pred[0] * 100, 1)
            duck_prob = round(pred[1] * 100, 1)
            print(cat_prob, duck_prob)
            print(path_image)
    return render_template('response.html', path_image=path_image, cat_prob=cat_prob, duck_prob=duck_prob)
