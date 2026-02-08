import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    #2D array representation of buttons
    BUTTON_LAYOUT = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", "C", "=", "+"],
    ]
    
    #Initialize UI
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")
        
        self.calculator = Calculator()
        
        self._build_ui()
        
    def _build_ui(self):
        #Set display text to update when it changes
        self.display_var = tk.StringVar(value="0")
        
        #Create main field for widget
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 18),
            justify="right",
            bd=10
        )
        #Put display in top row of grid
        display.grid(row=0, column=0, columnspan=4,sticky="nsew")
        
        #Build button layout
        self._build_buttons()     
            
    def _build_buttons(self):
        #Place each button in appropriate place based on BUTTON_LAYOUT
        for row_index, row in enumerate(self.BUTTON_LAYOUT, start=1):
            for col_index, label in enumerate(row):
                #Pass each button its row,col position and value
                self._create_button(label, row_index, col_index)

    def _create_button(self, label, row, col):
        #Create new button with passed in value
        btn = tk.Button(
            self.root,
            text=label,
            font=("Arial", 14),
            command=lambda l=label: self.on_button_press(l) #Action for when button is pressed
        )

        #Place button in grid
        btn.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=2,
            pady=2
        )

    #Method which handles all button press
    def on_button_press(self, value):
        try:
            if value.isdigit():
                self.calculator.input_digit(value)
            elif value in "+-*/":
                self.calculator.set_operator(value)
            elif value == "=":
                self.calculator.calculate()
            elif value == "C":
                self.calculator.clear()

            self.display_var.set(self.calculator.get_display())

        #If value error, reset calculator and display ERROR
        except ValueError:
            self.calculator.clear()
            self.display_var.set("ERROR")

#Create new Tkinter widget on run        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()