from tkinter import Tk
from calcGUI import CalculatorGUI

def main():
    root = Tk()
    app = CalculatorGUI(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()