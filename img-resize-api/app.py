from flask import Flask, request
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route("/resize", methods=['POST'])
def resize_to_384_x_384():
    # download image
    response = requests.get(request.get('img_url'))
    img_name = request.get('img_name')
    original_image = Image.open(BytesIO(response.content))

    # resize image
    resized_image = original_image.resize((384, 384))

    # upload image back
    files= {'image': (img_name,resized_image,'multipart/form-data') }
    img_resize_resp = requests.post('http://img-upload-api/upload', files=files)
    return img_resize_resp

