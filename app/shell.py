import kivy
from kivy.app import App


kivy.require('1.8.0')


class Shell(App):
    def build(self):
        # the root is created in footch.kv
        root = self.root

