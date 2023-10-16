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



#java syntax 

# public class Dog {
    ##### Instance Variables
#     String name;
#     String breed;
#     int age;
#     String color;
 
    ##### Constructor Declaration of Class
#     public Dog(String name, String breed, int age,
#                String color)
#     {
        # HERE THIS WORKS LIKE SELF OF PYTHON
#         this.name = name;
#         this.breed = breed;
#         this.age = age;
#         this.color = color;
#     }
 
#     ##### method 1
#     public String getName() { return name; }
 
#     ##### method 2
#     public String getBreed() { return breed; }
 
#     ##### method 3
#     public int getAge() { return age; }
 
#     ##### method 4
#     public String getColor() { return color; }
 
#     @Override public String toString()
#     {
#         return ("Hi my name is " + this.getName()
#                 + ".\nMy breed,age and color are "
#                 + this.getBreed() + "," + this.getAge()
#                 + "," + this.getColor());
#     }
 
#     public static void main(String[] args)
#     {
#         Dog tuffy = new Dog("tuffy", "papillon", 5, "white");
#         System.out.println(tuffy.toString());
#     }
# }




# VVVVVVVIMP  Here in Kotlin syntax is a bit different in kotlie we use the parethsis and with the class name itself and all the varaible declared with val/var are the attributes of class
## Koltin Syntax 

# fun main(args: Array<String>) {
#     val emp = employee(18018, "Sagnik")
#     // default value for emp_name will be used here
#     val emp2 = employee(11011)
#     // default values for both parameters
#       // because no arguments passed
#     val emp3 = employee()
# }
 
# class employee(val emp_id : Int = 100 , emp_name: String = "abc") {
#     
#      var name: String
 
#     // initializer block
#     init {
#         
#         name = emp_name
 
#         print("Employee id is: $id, ")
#         println("Employee name: $name")
#         println()
#     }
# }