from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser

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



if __name__ == "__main__":
    FileChooser().run()

