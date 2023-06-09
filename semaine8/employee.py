class Employee:

    message = "Class Employee" # variable statique

    def __init__(self , name , position , age , salary , experience) :
        ## instance attributes
        print ("I am the constructor of the Employee's class")
        self.__name = name   
        self.position = position   # public
        self.age = age
        self.__salary = salary  # private
        self.experience = experience 
    
    def introduire(self):
        print(f"I am {self.name} and I am {self.age} year.")

    # def myName(self,):
    #     return self .myName
# class Bombe:
#     def __init__(self, ):
#         self.__start = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name( self , n ):
        self.__name = n 

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self , n):
        self.__salary = n


    def __str__(self) :
        return  f"I am {self.__name}. "

# creation of an object of type Employee 
employee1 = Employee ("Pierre" , "Developpeur" , 25 , 80000 , 2 )
print(employee1)

print("--  --  --  --  --  --")
print (employee1.experience)
employee1.introduire()
print (employee1.name)

employee1.name = "Ali"
print (employee1.name)
print (employee1.salary)
print (Employee.message)
employee1.salary = 100000
print (employee1.salary)

# print (employee1.__salary)   # False
print("--  --  --  --  --  --")

employee2 = Employee ("Alain" , "Ingenieru" , 28 , 86000 , 4 )
employee2.introduire()

# print (employee2.age)
# print (employee2.name)

