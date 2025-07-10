from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import json
import time
import os

Window.clearcolor = (0.1, 0.1, 0.1, 1)

# ---------- Prediction Popup ----------
class PredictionPopup(Popup):
    def __init__(self, match, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Prediction: {match['home']} vs {match['away']}"
        self.ids.pred_label.text = f"""
📊 {match['home']} vs {match['away']}
⏳ Kickoff: {match['time_left']} mins

✅ Prediction: {match['prediction']}
🔥 Tip: {match['tip']}

➡️ BTTS: {match['btts']}
📉 Over/Under: {match['over_under']}
🛡️ Double Chance: {match['double_chance']}
"""

# ---------- Screens ----------
class MainScreen(Screen):
    def on_pre_enter(self):
        self.load_matches()

    def load_matches(self):
        self.ids.match_list.clear_widgets()
        with open("matches.json", "r") as f:
            matches = json.load(f)

        for match in matches:
            self.ids.match_list.add_widget(
                MatchCard(match=match, manager=self.manager)
            )

class SavedScreen(Screen):
    def on_enter(self):
        self.ids.saved_list.clear_widgets()
        if os.path.exists("saved.json"):
            with open("saved.json", "r") as f:
                matches = json.load(f)
            for match in matches:
                self.ids.saved_list.add_widget(
                    MatchCard(match=match, manager=self.manager)
                )

# ---------- Match Card ----------
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.label import Label

class MatchCard(BoxLayout):
    def __init__(self, match, manager, **kwargs):
        super().__init__(orientation='vertical', size_hint_y=None, height='180dp', padding=10, spacing=5, **kwargs)
        self.match = match
        self.manager = manager

        # Logos and title
        h = BoxLayout(size_hint_y=None, height='50dp')
        h.add_widget(AsyncImage(source=match["home_logo"]))
        h.add_widget(Label(text=f"{match['home']} vs {match['away']}", halign='center', color=(1,1,1,1)))
        h.add_widget(AsyncImage(source=match["away_logo"]))
        self.add_widget(h)

        self.add_widget(Label(text=f"League: {match['league']} - Kickoff in {match['time_left']} mins", color=(0.9, 0.9, 0.9, 1)))
        self.add_widget(Label(text=f"Prediction: {match['prediction']} | BTTS: {match['btts']} | O/U: {match['over_under']}", color=(0.8, 0.8, 0.8, 1)))

        btns = BoxLayout(size_hint_y=None, height='40dp')
        btns.add_widget(Button(text="Details", on_release=lambda x: self.show_popup()))
        btns.add_widget(Button(text="Save", on_release=lambda x: self.save_match()))
        self.add_widget(btns)

    def show_popup(self):
        pop = PredictionPopup(match=self.match)
        pop.open()

    def save_match(self):
        if os.path.exists("saved.json"):
            with open("saved.json", "r") as f:
                saved = json.load(f)
        else:
            saved = []

        if self.match not in saved:
            saved.append(self.match)
            with open("saved.json", "w") as f:
                json.dump(saved, f)
            print("✅ Match saved")

# ---------- Screen Manager ----------
class ScreenManagement(ScreenManager):
    pass

# ---------- App ----------
class BettingHubApp(App):
    def build(self):
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    BettingHubApp().run()