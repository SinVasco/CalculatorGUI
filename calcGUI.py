from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        # Set the background color similar to iOS calculator
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # Main layout container
        layout = BoxLayout(orientation='vertical')

        # Display Label
        self.display = Label(text='0', font_size=40, halign='right', valign='middle', size_hint=(1, 0.2), color=(1, 1, 1, 1), width = 400)
        self.display.bind(size=self.display.setter('text_size'))  # Bind size to allow for proper text resizing
        layout.add_widget(self.display)


        grid = GridLayout(cols=4, spacing=10, padding=10)

        # Button definitions (text, color)
        buttons = [
            ('AC', (0.6, 0.6, 0.6, 1)), ('+/-', (0.6, 0.6, 0.6, 1)), ('%', (0.6, 0.6, 0.6, 1)), ('/', (1, 0.6, 0, 1)),
            ('7', (0.8, 0.8, 0.8, 1)), ('8', (0.8, 0.8, 0.8, 1)), ('9', (0.8, 0.8, 0.8, 1)), ('*', (1, 0.6, 0, 1)),
            ('4', (0.8, 0.8, 0.8, 1)), ('5', (0.8, 0.8, 0.8, 1)), ('6', (0.8, 0.8, 0.8, 1)), ('-', (1, 0.6, 0, 1)),
            ('1', (0.8, 0.8, 0.8, 1)), ('2', (0.8, 0.8, 0.8, 1)), ('3', (0.8, 0.8, 0.8, 1)), ('+', (1, 0.6, 0, 1)),
            ('0', (0.8, 0.8, 0.8, 1)), ('.', (0.8, 0.8, 0.8, 1)), ('=', (1, 0.6, 0, 1))
        ]

        # Create buttons using a loop
        for text, bg_color in buttons:
            btn = Button(text=text, background_color=bg_color, font_size=24, color=(0, 0, 0, 1) if bg_color[0] > 0.7 else (1, 1, 1, 1))
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        layout.add_widget(grid)
        return layout

    def on_button_press(self, instance):
        # Update display text based on button pressed
        if instance.text == 'AC':
            self.display.text = '0'
        elif instance.text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = 'Error'
        elif instance.text == '%':
            self.display.text += '/ 100'
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = 'Error'
        elif instance.text == '+/-':
            self.display.text = f'-1*({self.display.text})'
        elif self.display.text == '0':
            self.display.text = instance.text
        else:
            self.display.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()