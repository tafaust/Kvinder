import kivy
from kivy.factory import Factory
from kivy.app import App


kivy.require('1.8.0')


class Shell(App):
    def build(self):
        # the root is created in shell.kv
        root = self.root


# register widgets
Factory.register('Swiper', module='app.widgets')
Factory.register('Card', module='app.widgets')

