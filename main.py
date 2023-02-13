# # from kivy.app import App
# # from kivy.uix.label import Label

# # class BasicApp(App):
# #     def build(self):
# #         label = Label(text="Hdddd")
# #         return label

# # app = BasicApp()
# # app.run()


# from kivymd.app import MDApp
# from kivy.uix.carousel import Carousel
# from kivy.uix.image import Image
# from kivymd.theming import ThemeManager
# from kivymd.uix.card import MDCard
# from kivymd.uix.floatlayout import MDFloatLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.label import MDLabel

# class MDFloatLayoutApp(MDApp):
#     theme_cls = ThemeManager()
#     def build(self):
#         float_layout = MDFloatLayout()
#         card = MDCard(size_hint=(.45, .8), pos_hint={"center_x": .5, "center_y": .5})
#         float_layout.add_widget(card)
#         label = MDLabel(text="Manage Closet",bold=True,pos_hint={"center_x": .88, "center_y": .8},font_style="H4")
#         float_layout.add_widget(label)
#         carousel = Carousel(direction='right')
#         for i in range(4):
#             layout = MDFloatLayout()
#             text_field = MDTextField(id="username",hint_text="Username",size_hint_x=.8,pos_hint={"center_x": .5, "center_y": .48})
#             layout.add_widget(text_field)
#             carousel.add_widget(layout)
#         card.add_widget(carousel)

# if __name__ == '__main__':
#     MDFloatLayoutApp().run()



from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a BoxLayout for the login form
        self.form_container = BoxLayout(orientation="vertical")

        # Create the username TextInput
        self.username = TextInput(hint_text="Username")
        self.form_container.add_widget(self.username)

        # Create the password TextInput
        self.password = TextInput(hint_text="Password", password=True)
        self.form_container.add_widget(self.password)

        # Create the login button
        self.login_button = Button(text="Login", size_hint_y=None, height=50)
        self.login_button.bind(on_release=self.login)
        self.form_container.add_widget(self.login_button)

        # Add the form_container to the screen
        self.add_widget(self.form_container)

    def login(self, instance):
        # Get the values of the username and password
        username = self.username.text
        password = self.password.text

        # Check if the username and password are valid
        if username == "admin" and password == "password":
            # Change to the upload screen
            self.manager.current = "upload"
        else:
            # Show an error message
            self.form_container.add_widget(Label(text="Incorrect username or password", font_size=20, color=(1, 0, 0, 1)))

class UploadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a BoxLayout for the upload form
        self.form_container = BoxLayout(orientation="vertical")

        # Create a label for the upload form
        self.form_container.add_widget(Label(text="Upload a Picture:", font_size=20))

        # Create the FileChooserIconView
        self.file_chooser = FileChooserIconView()
        self.form_container.add_widget(self.file_chooser)

        # Create the upload button
        self.upload_button = Button(text="Upload", size_hint_y=None, height=50)
        self.upload_button.bind(on_release=self.upload_picture)
        self.form_container.add_widget(self.upload_button)

        # Add the form_container to the screen
        self.add_widget(self.form_container)

    def upload_picture(self, instance):
        # Get the selected file
        file = self.file_chooser
        
class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add the login and upload screens to the ScreenManager
        self.add_widget(LoginScreen(name="login"))
        self.add_widget(UploadScreen(name="upload"))

class LoginUploadApp(App):
    def build(self):
        # Create an instance of the AppScreenManager
        return AppScreenManager()

if __name__ == "__main__":
    LoginUploadApp().run()
