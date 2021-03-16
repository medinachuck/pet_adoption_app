from flask import Flask, render_template, redirect, url_for, request, flash
#from fastai.basic_train import load_learner
from fastai.vision.all import *
#from fastai.vision import open_image
#from flask_cors import CORS,cross_origin
# import jpeg's
import os
from random import choice
from flask import url_for, render_template
from werkzeug.utils import secure_filename
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


# 2. Create an app
app = Flask(__name__)
#CORS(app, support_credentials=True)
#learn = load_learner(path='./static/models', file='adoption_model.pkl')
# learn = load_learner("./static/models/adoption_model.pkl")
#classes = learn.data.classes


# User image upload
UPLOAD_FOLDER = '/static/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('static', 'UPLOAD_FOLDER', filename))
            #Use the filename with the filepath as an input to the model.predict()
            


            
            #Then with the results pass to a results page and redirect
            return redirect('/')
    return 





# BASICS
# 3. Define static routes
@app.route("/")
def index():
    return render_template('poundpuppy.html')



@app.route("/api/sen")
def sen_data():

    # SQL to json guide: https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python 

    # add json to the /api route

    # go back to main when done
    return data_jsons.sen_json()

@app.route("/api/attr")
def attr_data():

    # SQL to json guide: https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python 

    # add json to the /api route

    # go back to main when done
    return data_jsons.attr_json()


@app.route("/api/relig")
def relig_json():

    # SQL to json guide: https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python 

    # add json to the /api route

    # go back to main when done
    return data_jsons.relig_json()

# more routes to include:
# other Pet adoption Pages




#     # Return template and data
#     return render_template("index.html", vacation=destination_data)

# code for jpeg import
@app.route('/random_image')
def random_image():
    names = os.listdir(os.path.join(app.static_folder, 'img\Headshots\headshots'))
    # img_url = url_for('static', filename=os.path.join('img\Headshots\headshots', choice(names)))
    return render_template('random_image.html', names=names)


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

#5. User input for pet image
