from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class ColSpanApp(App):
    def build(self):
        grid = GridLayout(cols=4)

        # Button that simulates spanning two columns
        span_button = Button(text='Span 2 Columns', size_hint_x=None, width=200)
        grid.add_widget(span_button)

        # Other buttons
        for i in range(3):  # Only three more buttons on this row to total 4 columns
            grid.add_widget(Button(text=f'Button {i+1}'))

        # Fill in more rows normally
        for i in range(8):  # Add 8 more buttons to fill 2 more rows
            grid.add_widget(Button(text=f'Button {i+5}'))

        return grid

if __name__ == '__main__':
    ColSpanApp().run()
