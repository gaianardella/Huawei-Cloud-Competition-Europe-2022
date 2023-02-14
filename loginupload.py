from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import os

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)
        self.username_input = TextInput(text='', size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .6})
        self.password_input = TextInput(text='', size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .5}, password=True)
        self.login_button = Button(text='Login', size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .4})
        self.login_button.bind(on_press=self.login)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)

    def login(self, instance):
        # TODO: authenticate user's credentials
        if self.username_input.text == 'user' and self.password_input.text == 'pass':
            self.manager.current = 'upload_screen'

class UploadScreen(Screen):
    def __init__(self, **kwargs):
        super(UploadScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)
        self.file_chooser = FileChooserListView(size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .6})
        self.upload_button = Button(text='Upload', size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y': .2})
        self.upload_button.bind(on_press=self.upload)
        layout.add_widget(self.file_chooser)
        layout.add_widget(self.upload_button)

    def upload(self, instance):
        filename = self.file_chooser.selection and self.file_chooser.selection[0] or None
        if filename is not None:
            # TODO: upload file to server
            with open(filename, 'rb') as file:
                image_data = file.read()
                image = Image(texture=image_data)
                self.add_widget(image)

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.login_screen = LoginScreen(name='login_screen')
        self.upload_screen = UploadScreen(name='upload_screen')
        self.add_widget(self.login_screen)
        self.add_widget(self.upload_screen)

class MyApp(App):
    def build(self):
        screen_manager = ScreenManagement()
        return screen_manager

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    MyApp().run()
