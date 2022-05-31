__version__ = "1.0.4"
import kivy
kivy.require('2.1.0')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton, MDFloatingActionButton, MDFlatButton, MDRoundFlatButton
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from main_kv import KV_FILE
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
import pandas as pd
import random

value = 500
# Generating Random Words in Japanese

data = pd.read_csv("images/N5.csv")
obj = {}
lis = []
for i in range(0, value):
    obj["Kana"] = data.kana[i]
    obj["Eng"] = data.english[i]
    obj["Kanji"] = data.kanji[i]
    obj["type"] = data.type[i]
    obj_copy = obj.copy()
    lis.append(obj_copy)

class HindiWordEdit(Screen):
    pass


class About(Screen):
    pass


class Home(Screen):
    pass
       
class Content(MDBoxLayout):
    screen_manager = ObjectProperty()
    def begin(self):
        self.value = 100
        self.screen_manager.current("main")
    # def easy(self):
    #     self.value = 500
    # def moderate(self):
    #     self.value = 1000
    # def advance(self):
    #     self.value = 2000


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class KinbanApp(MDApp):
    dialog = None           
    def __init__(self, **kwargs) -> None:
        super().__init__()
    def build(self):
        self.screen = Builder.load_string(KV_FILE)
        return self.screen
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Choose your level?", size_hint = (0.8, 1)
                ,type = "custom",
                content_cls = Content()
            )
        self.dialog.open()
    # def on_start(self):
    #     self.show_alert_dialog()
    



class MainScreen(Screen):
    screen_manager = ObjectProperty()
    def __init__(self, **kwargs) -> None:
        self.ran = random.choice(lis)
        self.curr = self.ran
        if type(self.curr["Kanji"]) != type(self.curr["Kana"]):
            self.japanese = self.curr["Kana"]
        else:
            self.japanese = self.curr["Kanji"]
        super().__init__(**kwargs)
    
    def do(self):
        self.ids["card"].md_bg_color = get_color_from_hex("#afe3cf")
        self.ids["word"].text = self.curr["Eng"]
        self.ids["type"].text = ""
        self.ids["kana_word"].text = ""

    def next(self):
        self.ran = random.choice(lis)
        self.curr = self.ran
        if type(self.curr["Kanji"]) != type(self.curr["Kana"]):
            self.japanese = self.curr["Kana"]
        else:
            self.japanese = self.curr["Kanji"]
        self.ids["card"].md_bg_color = get_color_from_hex("#a4d9f5")
        self.ids["word"].text = self.japanese
        self.ids["type"].text = f'word type:{self.curr["type"]}'
        self.ids["kana_word"].text = f'({self.curr["Kana"]})'


KinbanApp().run()