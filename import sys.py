import os
import shutil
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from PIL import Image

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    padding: 20
    FileChooserListView:
        id: file_chooser
        filters: ['*.jpg', '*.jpeg', '*.png']
    Button:
        text: 'Convert to PDF'
        on_press: root.convert_to_pdf()
''')

class RootWidget(BoxLayout):
    def convert_to_pdf(self):
        file_path = self.ids.file_chooser.selection[0]
        file_name = os.path.basename(file_path)
        pdf_name = os.path.splitext(file_name)[0] + '.pdf'
        pdf_path = os.path.join(os.path.dirname(file_path), pdf_name)
        with Image.open(file_path) as im:
            im.save(pdf_path, "PDF", resolution=100.0)
        popup = Popup(title='PDF created', content=Label(text='PDF file saved as {}'.format(pdf_name)), size_hint=(0.8, 0.3))
        popup.open()

class MyApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MyApp().run()
