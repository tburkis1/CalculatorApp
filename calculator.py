class Calculator:
    
    #Initialize calculator class 
    def __init__(self):
        self.clear()
        
    def clear(self):
        #Reset calculator state
        self.current_value = "0"
        self.stored_value = None
        self.operator = None
        self.reset_input = False  
      
    def input_digit(self, digit: str):
        #If reset_input is true, start a new number with incoming digit
        if self.reset_input:
            self.current_value = digit
            self.reset_input = False
        #Reset_number is false, append new digit
        else:
            if self.current_value == "0":
                self.current_value = digit
            else:
                self.current_value += digit
    
    def set_operator(self, operator: str):
        #Evaluates existing expression if there is one. Allows chaining
        #Must enter a new number each time
        if self.operator is not None and not self.reset_input:
            self.calculate()

        #Store existing value, set operator and typing new number
        self.stored_value = int(self.current_value)
        self.operator = operator
        self.reset_input = True
        
    def flip_sign(self):
        #Do not allow sign flip after choosing an operator and before typing a number
        if not self.operator or (self.operator and not self.reset_input):
            value = int(self.current_value)
            self.current_value = str(-value)

    def calculate(self):
        #No existing value or expression do nothing
        if self.operator is None or self.stored_value is None:
            return

        current = int(self.current_value)

        #Find selected operator and perform that on stored and current
        if self.operator == "+":
            result = self.stored_value + current
        elif self.operator == "-":
            result = self.stored_value - current
        elif self.operator == "*":
            result = self.stored_value * current
        elif self.operator == "/":
            if current == 0:
                raise ValueError("Cannot divide by zero") #Cannot divide by zero raise error
            result = self.stored_value // current
        elif self.operator == "/":
            if current == 0:
                raise ValueError("Cannot divide by zero") #Cannot divide by zero raise error
            result = self.stored_value // current
        
        #Set current value and reset typing and stored
        self.current_value = str(result)
        self.stored_value = None
        self.operator = None
        self.reset_input = True
    
    #Display current number (result or user typing)
    def get_display(self) -> str:
        return self.current_value
