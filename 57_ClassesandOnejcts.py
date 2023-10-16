class Person :
    
    # these are the attributes of the class
    name = "Swarup"
    occupation = "Software Dev"
    age = 22 
    
    def info(self):
        print(f"The name of this Vyakti is `{self.name}` and it's age is : `{self.age}`")


p1 = Person()
p1.info()

# class : blueprint 
# object : instance of class
# self = references to the current object of class like in this case p1