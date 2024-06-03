from calclogic import CalculatorLogic
from tkinter import Frame, Entry, Button, N, S, E, W
import tkinter as tk

class CalculatorGUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.logic = CalculatorLogic()
        self.init_ui()

    def init_ui(self):
        self.master.title("GUI Calculator")
        self.pack(expand=False, fill='both')
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=('Arial', 24), bg='#333', fg='white', bd=0, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='news')

        self.master.grid_rowconfigure(0, weight=1)

        for i in range(1,5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)
        
        btn_labels = [
            ('AC', 'black', 'white'), ('+/-', 'lightgray', 'black'), ('%', 'lightgray', 'black'), ('/', 'orange', 'white'),
            ('7', 'black', 'white'), ('8', 'black', 'white'), ('9', 'black', 'white'), ('*', 'orange', 'white'),
            ('4', 'black', 'white'), ('5', 'black', 'white'), ('6', 'black', 'white'), ('-', 'orange', 'white'),
            ('1', 'black', 'white'), ('2', 'black', 'white'), ('3', 'black', 'white'), ('+', 'orange', 'white'),
            ('0', 'black', 'white'), ('.', 'black', 'white'), ('=', 'orange', 'white')
        ]

        r = 1
        c = 0

        for text, bg, fg in btn_labels:
            if text:
                btn = tk.Button(self, text=text, activebackground='black', fg=fg, font=('Arial', 20), bd=0,
                                command=lambda b=text: self.on_button_press(b))
                btn.grid(row = r, column = c, sticky='news')
                if text == '0':
                    self.grid_columnconfigure(0, weight=2)
                    btn.grid(columnspan=2, sticky='news')
                    c += 1
            c += 1
            if c > 3:
                c = 0
                r += 1
                
    def on_button_press(self, button):
        print(button)  # Logic to update the display or perform calculations
    def press(self, key):
        # Update display based on button press
        pass
