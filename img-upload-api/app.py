import os
import uuid
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)), "images")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return "<p>Hello, World! IMAGE UPLOAD API</p>"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_image_to_be_resized():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(str(uuid.uuid4()) + "-" + file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))

    return '''
    <!doctype html>
    <title>Enviar imagem</title>
    <h1>Enviar imagem para ser redimensionada para 384x384</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Enviar>
    </form>
    '''

@app.route('/uploads/<name>', methods=['GET'])
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)