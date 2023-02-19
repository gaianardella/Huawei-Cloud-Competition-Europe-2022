from obs import ObsClient, CorsRule, Options
from datetime import datetime
import boto3
import os
import pandas as pd
import pickle

# from huaweicloudsdkobs.obs_client import ObsClient
from huaweicloudsdkcore.auth.credentials import BasicCredentials

# Replace these with your own values
endpoint = "http://obs.eu-west-101.myhuaweicloud.eu"
server="obs.eu-west-101.myhuaweicloud.eu"
access_key = ""
secret_key = ""
bucket_name = ""
expire_seconds = 3600

obsClient = ObsClient(access_key_id='', secret_access_key='', server='obs.eu-west-101.myhuaweicloud.eu')
resp=obsClient.getObject(bucketName="outfits", objectKey='pairs/my_model.pickle')
# data = resp['body'].read()
response_wrapper = resp.body['response']
content = response_wrapper.read() #LEGGE I BITES!!!!!!!!!!!!!!!!!!!!!!
# print(content) #VEDO I BITES!!!!!!!!!!!!!!!!!!!!!!


new_input = pd.DataFrame({'color_1': ['red'], 'color_2': ['green']})
color_dict = {'black': 0, 'white': 1, 'grey': 2, 'red': 3, 'blue': 4, 'green': 5, 'yellow': 6, 'purple': 7, 'pink': 8}
new_input = new_input.replace(color_dict)

import pickle
model = pickle.loads(content)
prediction = model.predict(new_input)
print(prediction) #FUNZIONAAAAAAAAAAAAAAAAAAA

# with open('my_model.pickle', 'wb') as f:
#     f.write(resp.body)
