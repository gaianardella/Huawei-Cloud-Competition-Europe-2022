from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from obs import ObsClient, CorsRule, Options
from datetime import datetime
# import huaweicloud
import boto3
import os

# from huaweicloudsdkobs.obs_client import ObsClient
from huaweicloudsdkcore.auth.credentials import BasicCredentials

# Replace these with your own values
endpoint = "http://obs.eu-west-101.myhuaweicloud.eu"
server="obs.eu-west-101.myhuaweicloud.eu"
access_key = "JAKGEFBQBLHWUNWWGIGI"
secret_key = "3lRysHwqAlRnw7kVFSWRCZFuIbdHau6UYHfzObz3"
bucket_name = "clothes"
expire_seconds = 3600

obsClient = ObsClient(access_key_id='', secret_access_key='', server='obs.eu-west-101.myhuaweicloud.eu')

kv="""
MDFloatLayout:
    Image:
        id: img
    MDRaisedButton:
        text: "Upload"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release:
            app.file_chooser()
    MDLabel:
        id: selected_path
        text:""
        halign: "center"

"""

class FileChooser(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.root.ids.img.source = selection[0]

            print(selection[0]) #è il path della foto selezionata
            file_path = selection[0]

            print(type(file_path))
            #bucketClient = obsClient.bucketClient('clothes')
        
            # Getting the current date and time
            dt = datetime.now()
            # getting the timestamp
            ts = datetime.timestamp(dt)

            # resp = bucketClient.putContent('top' + str(ts), file.read())
            #resp = obsClient.putFile('clothes', 'top', file)

            obsClient.putFile('clothes',str(ts), file_path)


            #kivy_venv\Scripts\activate





if __name__ == "__main__":
    FileChooser().run()

