import kivy

from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


### Déclaration des widget

class MainWidget(BoxLayout): 
     



class MainApp(MDApp):

    def build(self):
        return MainWidget()

    def onstart():
        pass 

 

if '__name__' =='_ _main__':
    MainApp().run