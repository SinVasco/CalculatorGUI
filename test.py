from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window, Keyboard
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.window import Keyboard

class KeyboardApp(App):
    def build(self):
        self.label = Label(text="Type something...", font_size='20sp')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)

        self._keyboard  = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        # Bind the keyboard to the on_key_down callback
        #Window.bind(on_key_down=self.on_key_down)
        return layout

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        return True

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        # keycode[1] is the text of the key pressed
        # Update the label text to show the last key pressed
        print(keycode[1])
        #self.label.text = f'Last key pressed: {text} (Keycode: {keycode[1]})'

if __name__ == '__main__':
    KeyboardApp().run()
