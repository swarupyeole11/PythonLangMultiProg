class person:
    outside_var : int 

    def __init__(self,names,ages):
       self.outside_var = "outside_constructor_variable"
       self.inside_var = "inside_constructor_variable"
       self.name = names
       self.age = ages
    
    def info(self):
        print(f"You can declare attributes outside the constructer take e.g of  : {self.outside_var}")
    
p1 = person("swarup",23)
p1.info()

#  constrcutor is a special methid that helps in intializing the objects and is executed automatically every time an object is instatiated

class multi_person:

    name : str
    age : int
    marks : dict

    def __init__(self):
        print("empty constructor was called")
    
    def __init__(self,name,age,marks):
        self.marks = marks
        self.name = name
        self.age = age
        print(f"The marks obtained by {self.name} are {self.marks}")

#just to show that constructor is executed emvery time a function is called 
p1 = multi_person("swarup",21,{'chemistry': 98, 'maths' : 100})



#df
#