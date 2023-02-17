from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from obs import ObsClient, CorsRule, Options
from datetime import datetime
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

obsClient = ObsClient(access_key_id='X8KGMVB3Q0CGVULR5YX4', secret_access_key='RqFFvphp2wTdkKqRYMLqKBk8KsL0mBRWs1vRfFQP', server='obs.eu-west-101.myhuaweicloud.eu')

#fix for android app size
# from kivy.core.window import Window
# Window.size=(320,600)

KV="""

MDFloatLayout:
    MDCard:
        size_hint: .45, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        Carousel:
            id: slide
            MDFloatLayout:
                MDTextField:
                    id: username
                    hint_text: "Username"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    id: password
                    hint_text: "Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                    password: True
                MDRaisedButton:
                    text: "REGISTER"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .2}
                    on_release: app.register()
                MDRaisedButton:
                    text: "LOGIN"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}
                    on_release: app.login()     
            MDFloatLayout:
                MDLabel:
                    text: "What clothing item do you want to upload?"
                    bold: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_style: "H4"
                MDRaisedButton:
                    text: "Sweater"
                    size_hint_x: .39
                    pos_hint: {"center_x": .2, "center_y": .3}
                    on_release: app.next(self.text)
                MDRaisedButton:
                    text: "T-Shirt"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .3}
                    on_release: app.next(self.text)
                MDRaisedButton:
                    text: "Trousers"
                    size_hint_x: .39
                    pos_hint: {"center_x": .2, "center_y": .2}
                    on_release: app.next(self.text)
                MDRaisedButton:
                    text: "Shorts"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}
                    on_release: app.next(self.text)
            MDFloatLayout:
                MDLabel:
                    text: "Upload photo"
                    bold: True
                    pos_hint: {"center_x": .6, "center_y": .5}
                    font_style: "H4"
                MDRaisedButton:
                    text: "UPLOAD"
                    size_hint_x: .39
                    pos_hint: {"center_x": .4, "center_y": .2}
                    on_release: app.next()
            
    MDLabel:
        text: "Manage Closet"
        bold: True
        pos_hint: {"center_x": .88, "center_y": .8}
        font_style: "H4"
    MDLabel:
        id: Name
        text: "Name"
        pos_hint: {"center_x": .808, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id:name
        icon: "numeric-1-circle"
        pos_hint: {"center_x": .34, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
    MDLabel:
        id: Upload
        text: "Choose"
        pos_hint: {"center_x": .958, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id: choice
        icon: "numeric-2-circle"
        pos_hint: {"center_x": .5, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"
    MDLabel:
        id: Submit
        text: "Upload"
        pos_hint: {"center_x": 1.12, "center_y": .7}
        font_style: "H6"
        theme_text_color: "Custom"
    MDIconButton:
        id: submit
        icon: "numeric-4-circle"
        pos_hint: {"center_x": .66, "center_y": .65}
        user_font_size: "35sp"
        theme_text_color: "Custom"

"""
#sotto MDIconButton
# MDProgressBar:
#         size_hint_x: .1
#         pos_hint: {"center_x": .42, "center_y": .65}
#Non funziona, fa barra verticale grossa anzichè piccola orizzontale

users={"admin":"psw"}
class ProjectApp(MDApp):
    def build(self):
        kv = Builder.load_string(KV)
        return kv

    def register(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        users[username]=password
        print(users)

    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        # Check if the username and password match a known user
        #if username == "admin" and password == "password":
        if username in users and users[username]==password:
            print("Login successful!")
            self.root.ids.slide.load_next(mode="next")
        else:
            print("Login failed.")
            # self.error_message.text = 'Incorrect username or password'
            self.root.ids.password.error_message ='Incorrect username or password'
        # self.root.ids.slide.load_next(mode="next")
        # self.root.ids.Name.text_color = self.theme_cls.primary_color

        #self.root.ids.progress.value = 100

        # self.root.ids.name.text_color = self.theme_cls.primary_color
        # self.root.ids.name.icon = "check-decagram"
        
    def next(self, item):
        print(item)
        # self.root.ids.slide.load_next(mode="next")
        # self.root.ids.Contact.text_color = self.theme_cls.primary_color
        #self.root.ids.progress.value = 100
        # self.root.ids.contact.text_color = self.theme_cls.primary_color
        # self.root.ids.contact.icon = "check-decagram"
        file_path=filechooser.open_file(on_selection=self.selected)
        file_path=file_path[0]

        #Getting the current date and time
        dt = datetime.now()
        # getting the timestamp
        ts = datetime.timestamp(dt)
        obsClient.putFile('clothes',item +'/'+str(ts), file_path)

    def selected(self, selection):
        if selection:
            # self.root.ids.img.source = selection[0]
            return selection[0]

            # print(selection[0]) #è il path della foto selezionata
            # file_path = selection[0]

    # def previous(self):
    #     self.root.ids.slide.load_previous()
    #     self.root.ids.name.text_color = 0, 0, 0, 1
    #     self.root.ids.Name.text_color = 0, 0, 0, 1
    #     self.root.ids.name.icon = "numeric-1-circle"
    
    # def previous1(self):
    #     self.root.ids.slide.load_previous()
    #     self.root.ids.contact.text_color = 0, 0, 0, 1
    #     self.root.ids.Contact.text_color = 0, 0, 0, 1
    #     self.root.ids.contact.icon = "numeric-2-circle"
app = ProjectApp()
app.run()



#NELLA PRIMA PAGINA DEVO FARE REGISTER/LOGIN NON NEXT e forgot password
#LA SECONDA PAGINA è UPLOAD
#LA TERZA è SCELTA ABITI
#POI FAI SUBMIT
