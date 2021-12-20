
from flask import Flask, render_template, request,flash, request, redirect, url_for
from flask_restful import Resource,Api, reqparse
# example of using a pre-trained model as a classifier
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16

import werkzeug
from werkzeug.utils import secure_filename
import os

#from flask_cors import CORS, cross_origin
from flask_cors import CORS




# Process image and predict label
def processImg(IMG):
        # load an image from file
    image = load_img(IMG, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # load the model
    model = VGG16()
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    # print the classification
    #print()
    return {"result":[label[1], label[2]*100]}





UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class HelloWorld(Resource):
    def get(self):
        return {"hello":"world"}

class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()
     file = args['file']
     if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result=processImg(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return result
     return file.filename
    






# Initializing flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api=Api(app)
#cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = "abftreepwnfgfsyenfjk"

api.add_resource(HelloWorld,"/")
api.add_resource(UploadImage,"/up")

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
