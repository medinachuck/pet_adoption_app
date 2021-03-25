from flask import Flask, render_template, redirect, url_for, request, flash
#from fastai.basic_train import load_learner
from fastai.vision.all import *
#from fastai.vision import open_image
from flask_cors import CORS
# import jpeg's
import os
from random import choice
# import jsonify_for_flask_app 
from flask import url_for, render_template
from werkzeug.utils import secure_filename
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
# 2. Create an app
app = Flask(__name__)
# CORS(app, support_credentials=True)


# User image upload
UPLOAD_FOLDER = '/static/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}

# set-up learner function 
def predict_single(path_to_img):
    #call learners on uploaded image and save output to variables
    learn_adopt = load_learner("static/models/adoption_model.pkl")
    learn_type = load_learner("static/models/type_model.pkl")
    learn_breed = load_learner("static/models/BreedModel.pkl")
    
    type_prediction = learn_type.predict(path_to_img)
    breed_prediction = learn_breed.predict(path_to_img)
    adopt_prediction = learn_adopt.predict(path_to_img)
    results = {
        'type': type_prediction[0],
        'breed': breed_prediction[0],
        'adopt': adopt_prediction[0]
    }
    return results

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
# @app.route('/', methods=['POST'])
def upload_file():
    # print("The upload function is running")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            # return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            # return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            print(f'{filename}')
            path_to_img = os.path.join('static', 'UPLOAD_FOLDER', filename)
            # print("I am on line 54")
            file.save(path_to_img)
            print("THE DATA IS FINALLY HERE!")
            results = predict_single(path_to_img)
            #Then with the results pass to a results page and redirect
            print(results)
            # return results

            # return redirect('http://127.0.0.1:5000/results', code=302)

    return render_template('poundpuppy.html')

@app.route('/results')
def results_page():
    return render_template('results.html')


# about page route
@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)

#5. User input for pet image
