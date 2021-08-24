class flight:
   def __init__(self, number):
       if not number[:2].isalpha():
        raise ValueError(f"No airtime code in '{number}'")
       
       if not number[:2].isuper():
           raise ValueError(f"Invalid airtime code '{number}'")

        
       if not (number[2:].isidigit() and int(number[2:])<= 9999):
            raise ValueError(f"Invalid route number' {number}'")

       self._number = number
def number(self):
    return self._number

def airline(self):
    return self._number[:2]

class aircraft:
    def __init__(self, registration, model, num_rows,num_seats_per):
        self._registration = registration
        self._model = model
        
    
    def registration(self):
        return self._registration

    def model(self):
        return self._model

    
        