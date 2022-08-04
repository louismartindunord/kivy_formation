import kivy

from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


### Déclaration des widget



class MainApp(MDApp):

    def build(self):
        return MainWidget()

    #def onstart():
    #    pass 

class MainWidget(BoxLayout): 
    pass
     
if '__name__' == '__main.py__':
    MainApp.run()