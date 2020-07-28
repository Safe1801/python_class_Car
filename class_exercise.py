class Car: 
    '''Modelling a Car   <- ''' # Docstring 

    def __init__(self, model, license): #
       
       '''Initialize all attributes and properties'''
        
       self.model = model 
       self.license = license

    def drive(self): 
        print("VROOM VROOM! The car drives!")

    def honk(self):
        print("HONK HONK!")

    def mileage(self):
        val=input("What is the mileage? ")
        print(self.model + "Mileage: " + val)

class ElectricCar(Car): 
   
    ''' Child class '''
    
    def __init__(self, model, license): 
        super().__init__(model, license) # This is done so a connection can be made between the parent and the child.
        #  With super() it can access all attributes and methods of the parent class.
