class vehicle:
    def __init__(self, make, model, year):
        self.make =make
        self.model = model
        self.year = year
        
        
    def strart_engine(self):
        return f"the engine of the {self.year} {self.make} {self.model} is starting"
        
    def stop_engine(self):
        return f"the engine of the {self.year} {self.make} {self.model} is stopped"
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"vehicle(check='{self.make}',model='{self.model}',year={self.year})"    
        return f"{self.year} {self.make} {self.model}"
   