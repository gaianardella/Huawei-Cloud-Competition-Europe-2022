pip install scikit-learn

from obs import ObsClient
from PIL import Image

endpoint = "http://obs.eu-west-101.myhuaweicloud.eu"
server="obs.eu-west-101.myhuaweicloud.eu"
access_key = ""
secret_key = ""
# Set up OBS client
obs_client = ObsClient(access_key_id=access_key, secret_access_key=secret_key, server=server)


categories = {
    'Sweater': 'Trousers',
    'T-Shirt': 'Shorts'
}

# Convert the color names into numerical values
color_dict = {'black': 0, 'white': 1, 'grey': 2, 'red': 3, 'blue': 4, 'green': 5, 'yellow': 6, 'purple': 7, 'pink': 8}

resp = obs_client.listObjects('clothes')

files={'Sweater':[], 'T-Shirt':[], 'Trousers':[], 'Shorts':[]}
for item in resp['body']['contents']:
    temp_li=str(item).split('/')
    key = temp_li[0]
    if key in files:
        value = temp_li[1]
        files[key].append(value)
        
import pandas as pd
import pickle
import io
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from datetime import datetime


for el in files['T-Shirt']:
    for elem in files['Shorts']:
        
        color_1=el.split('_')[0].lower()
        color_2=elem.split('_')[0].lower()
        
        new_input = pd.DataFrame({'color_1': [color_1], 'color_2': [color_2]})
        new_input = new_input.replace(color_dict)
        
        with open('my_model.pickle', 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(new_input)
        
        if prediction == 'yes':
            
            resp1=obs_client.getObject(bucketName="clothes", objectKey='T-Shirt/' + str(el))
            response_wrapper1 = resp1.body['response']
            content1 = response_wrapper1.read()

            # Create a file-like object from the raw bytes
            img_file1 = io.BytesIO(content1)

            # Read the image data using imread
            img1 = mpimg.imread(img_file1, format='jpg')

            resp2=obs_client.getObject(bucketName="clothes", objectKey="Shorts/" + str(elem))
            response_wrapper2 = resp2.body['response']
            content2 = response_wrapper2.read()

            # Create a file-like object from the raw bytes
            img_file2 = io.BytesIO(content2)

            # Read the image data using imread
            img2 = mpimg.imread(img_file2, format='jpg')

            # Check the shape of the image arrays
            if img1.shape[0] < img1.shape[1]:
                img1 = np.rot90(img1, k=3)

            if img2.shape[0] < img2.shape[1]:
                img2 = np.rot90(img2, k=3)

            # Stack the two images horizontally
            img_horizontal = np.concatenate([img1, img2], axis=1)

            # Display the stacked image using imshow
            plt.imshow(img_horizontal)
            
            # assuming img_horizontal is a numpy array of shape (height, width, channels)
            # convert it to uint8 data type
            img_data = np.uint8(img_horizontal)

            # create a PIL image object from the numpy array
            img = Image.fromarray(img_data)
            
            #Getting the current date and time
            dt = datetime.now()

            # getting the timestamp
            ts = datetime.timestamp(dt)

            # save the image as a JPG file
            img.save(str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg")
            image = Image.open(str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg")
            
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            image_bytes = buffered.getvalue()

            obs_client.putContent("outfits","Hot/" +str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg",image_bytes)

        elif prediction == 'no':
            print(color_1+" and "+color_2+" cannot be combined")
import pandas as pd
import pickle
import io
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from datetime import datetime


for el in files['Sweater']:
    for elem in files['Trousers']:
        
        color_1=el.split('_')[0].lower()
        color_2=elem.split('_')[0].lower()
        
        new_input = pd.DataFrame({'color_1': [color_1], 'color_2': [color_2]})
        new_input = new_input.replace(color_dict)
        
        with open('my_model.pickle', 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict(new_input)
        
        if prediction == 'yes':
            
            resp1=obs_client.getObject(bucketName="clothes", objectKey='Sweater/' + str(el))
            response_wrapper1 = resp1.body['response']
            content1 = response_wrapper1.read()

            # Create a file-like object from the raw bytes
            img_file1 = io.BytesIO(content1)

            # Read the image data using imread
            img1 = mpimg.imread(img_file1, format='jpg')

            resp2=obs_client.getObject(bucketName="clothes", objectKey="Trousers/" + str(elem))
            response_wrapper2 = resp2.body['response']
            content2 = response_wrapper2.read()

            # Create a file-like object from the raw bytes
            img_file2 = io.BytesIO(content2)

            # Read the image data using imread
            img2 = mpimg.imread(img_file2, format='jpg')

            # Check the shape of the image arrays
            if img1.shape[0] < img1.shape[1]:
                img1 = np.rot90(img1, k=3)

            if img2.shape[0] < img2.shape[1]:
                img2 = np.rot90(img2, k=3)

            # Stack the two images horizontally
            img_horizontal = np.concatenate([img1, img2], axis=1)

            # Display the stacked image using imshow
            plt.imshow(img_horizontal)
            
            # assuming img_horizontal is a numpy array of shape (height, width, channels)
            # convert it to uint8 data type
            img_data = np.uint8(img_horizontal)

            # create a PIL image object from the numpy array
            img = Image.fromarray(img_data)
            
            #Getting the current date and time
            dt = datetime.now()

            # getting the timestamp
            ts = datetime.timestamp(dt)

            # save the image as a JPG file
            img.save(str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg")
            image = Image.open(str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg")
            
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            image_bytes = buffered.getvalue()

            obs_client.putContent("outfits","Cold/" +str(color_1)+"_"+str(color_2)+"_"+str(ts)+".jpg",image_bytes)

        elif prediction == 'no':
            print(color_1+" and "+color_2+" cannot be combined")

