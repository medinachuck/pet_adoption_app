from flask import Flask, render_template, redirect, url_for, request, flash
#from fastai.basic_train import load_learner
from fastai.vision.all import *
#from fastai.vision import open_image
from flask_cors import CORS, cross_origin
# import jpeg's
import os
from random import choice
import jsonify_for_flask_app as jData
from flask import url_for, render_template
from werkzeug.utils import secure_filename
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
import json
# 2. Create an app
app = Flask(__name__)
#CORS(app, support_credentials=True)


# User image upload
UPLOAD_FOLDER = '/static/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}

#learn = load_learner(path='./static/models', file='adoption_model.pkl')
learn_adopt = load_learner("static/models/adoption_model.pkl")
learn_type = load_learner("static/models/type_model.pkl")
learn_breed = load_learner("static/models/BreedModel.pkl")

# set-up learner function 
def predict_single(path_to_img):
    #call learners on uploaded image and save output to variables
    type_prediction = learn_type.predict(path_to_img)
    breed_prediction = learn_breed.predict(path_to_img)
    adopt_prediction = learn_adopt.predict(path_to_img)
    predict_result = [int(type_prediction[0]),int(breed_prediction[0]),int(adopt_prediction[0])]
    return predict_result

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # print("The upload function is running")
    data1 = {}
    global breed
    global peType
    global peAdo
    global path_1

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
            temp = predict_single(path_to_img)
            print(temp[0], temp[1],temp[2])
            breed = jData.id_breed(temp[1])
            peType = jData.id_type(temp[0])
            peAdo = jData.id_adopt(temp[2])
            path_1 = os.path.splitdrive(path_to_img)

            data1 ={
                'breed' : breed,
                'type' : peType,
                'adopt': peAdo,
                'image': path_1
                }
            # redirect
    # data1=json.dumps(data1, indent = 4)

    # output=tempDict
    print(data1)

    # return render_template("poundpuppy.html")
    return render_template("poundpuppy.html",data1=data1)

@app.route('/results')
def results_page():
    petinfo={}
    petinfo ={
        'breed' : breed,
        'type' : peType,
        'adopt': peAdo,
        'image': path_1
    }
    return render_template("results.html", petinfo = petinfo)



# about page route
@app.route("/about")
def about():
    print(breed)
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

#5. User input for pet image
