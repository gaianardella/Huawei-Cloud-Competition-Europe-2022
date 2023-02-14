from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# from kivy.lang import Builder

class Background(Widget):
    def __init__(self, **kwargs):
        #inserisco background
        super().__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(source='background.jpg', pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Create a dictionary to store the login information
        self.login_info = {'username': 'username', 'password': 'password'}
    
    def update_rect(self, *args):
        #prende dimensioni app e mette login di conseguenza
        self.rect.pos = self.pos
        self.rect.size = self.size

        # Position the login elements
        self.username_input.pos = (self.center_x - self.username_input.width/2, self.center_y + 50)
        self.password_input.pos = (self.center_x - self.password_input.width/2, self.center_y - 50)
        self.login_button.pos = (self.center_x - self.login_button.width/2, self.center_y - 150)

    def on_size(self, *args):
        self.update_rect()

    def on_pos(self, *args):
        self.update_rect()

    def add_login_elements(self):
        # Add a username TextInput to the background
        self.username_input = TextInput(hint_text='Username', size_hint=(None, None), size=(200, 50))
        self.add_widget(self.username_input)

        # Add a password TextInput to the background
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(None, None), size=(200, 50))
        self.add_widget(self.password_input)

        # Add a login Button to the background
        self.login_button = Button(text='Login', size_hint=(None, None), size=(200, 50))
        self.add_widget(self.login_button)

        #Aggiunge risposta del login
        self.login_button.bind(on_press=self.login)

    def login(self, instance):
        # Get the entered username and password
        username = self.username_input.text
        password = self.password_input.text

        # Check if the entered login information is valid
        if username == self.login_info['username'] and password == self.login_info['password']:
            print('Login successful')
            self.manager.current = 'second'
        else:
            print('Invalid login information')

    def switch_to_second_screen(self, *args):
        self.manager.current = 'second'


class FirstScreen(Screen):
    # def __init__(self, **kwargs):
    #     super(FirstScreen, self).__init__(**kwargs)
    #     self.add_widget(Label(text='Welcome to the First Screen!'))
    #     button = Button(text='Go to Second Screen', size_hint=(None, None), size=(200, 50))
    #     button.bind(on_press=self.switch_to_second_screen)
    #     self.add_widget(button)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create an instance of Background
        self.background = Background()
        self.background.add_login_elements()

        # add the background widget to the screen
        self.add_widget(self.background)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Welcome to the Second Screen!'))
        # button = Button(text='Go back to First Screen', size_hint=(None, None), size=(200, 50))
        # button.bind(on_press=self.switch_to_first_screen)
        # self.add_widget(button)

    # def switch_to_first_screen(self, *args):
    #     self.manager.current = 'first'


# class NewPage(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         label = Label(text='Do you want to continue?', pos_hint={'center_x': 0.5, 'center_y': 0.6})
#         self.add_widget(label)
#         yes_button = Button(text='Yes', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.4, 'center_y': 0.4})
#         no_button = Button(text='No', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.6, 'center_y': 0.4})
#         yes_button.bind(on_press=self.on_yes)
#         no_button.bind(on_press=self.on_no)
#         self.add_widget(yes_button)
#         self.add_widget(no_button)

    def on_yes(self, instance):
        print('Yes')
        # Do something here

    def on_no(self, instance):
        print('No')

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        self.icon="icon.png"
        Window.icon = 'icon.png'
        # background = Background()
        # background.add_login_elements()
        # return background
        screen_manager = MyScreenManager()
        screen_manager.add_widget(FirstScreen(name='first'))
        screen_manager.add_widget(SecondScreen(name='second'))
        return screen_manager

        
        # layout = BoxLayout(orientation0"vertical")


if __name__=="__main__":
    app = MainApp()
    app.run()

# app = MainApp()
# app.run()
# class MainApp(App):
#     def build(self):
        # label = Label(text="Hdddd")
        # return label


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



# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# # from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.filechooser import FileChooserIconView
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window

# Window.size=(320,600)
# Window.clearcolor = (0.749019608, 1.0, 0.792156863, 1)

# class LoginScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         # Create a BoxLayout for the login form
#         # self.form_container = BoxLayout(orientation="vertical", spacing=30, padding=30)
#         self.form_container = FloatLayout()
#         # Create the username TextInput
#         self.username = TextInput(hint_text="Username", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8})
#         self.form_container.add_widget(self.username)

#         # Create the password TextInput
#         self.password = TextInput(hint_text="Password", size_hint=(.6, .1), pos_hint={"x": .2, "y": .6}, password=True)
#         self.form_container.add_widget(self.password)

#         # Create the login button
#         self.login_button = Button(text="Login", size_hint=(.6, .1), pos_hint={"x": .2, "y": .4})
#         self.login_button.bind(on_release=self.login)
#         self.form_container.add_widget(self.login_button)

#         # Add the form_container to the screen
#         self.add_widget(self.form_container)

#     def login(self, instance):
#         # Get the values of the username and password
#         username = self.username.text
#         password = self.password.text

#         # Check if the username and password are valid
#         if username == "admin" and password == "password":
#             # Change to the upload screen
#             self.manager.current = "upload"
#         else:
#             # Show an error message
#             self.form_container.add_widget(Label(text="Incorrect username or password", font_size=20, color=(1, 0, 0, 1)))

# class UploadScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         # Create a BoxLayout for the upload form
#         # self.form_container = BoxLayout(orientation="vertical", spacing=30, padding=30)
#         self.form_container = FloatLayout()

#         # Create a label for the upload form
#         self.form_container.add_widget(Label(text="Upload a Picture:", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8}, bold=True))

#         # Create the FileChooserIconView
#         self.file_chooser = FileChooserIconView(path=".", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.4})
#         self.form_container.add_widget(self.file_chooser)

#         # Create the Browse button
#         # self.browse_button = Button(text="Browse", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.6})
#         # self.browse_button.bind(on_release=self.show_file_picker)
#         # self.add_widget(self.browse_button)

#         # Create the upload button
#         # self.upload_button = Button(text="Upload", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.4})
#         # self.upload_button.bind(on_release=self.upload_picture)
#         # self.form_container.add_widget(self.upload_button)

#         # Add the form_container to the screen
#         self.add_widget(self.form_container)

#     def upload_picture(self, instance):
#         # Get the selected file
#         file = self.file_chooser

# class AppScreenManager(ScreenManager):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         # Add the login and upload screens to the ScreenManager
#         self.add_widget(LoginScreen(name="login"))
#         self.add_widget(UploadScreen(name="upload"))

# class LoginUploadApp(App):
#     def build(self):
#         # Create an instance of the AppScreenManager
#         return AppScreenManager()

# if __name__ == "__main__":
#     LoginUploadApp().run()
