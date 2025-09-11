# ---------------------------- single inheirtence------------------

# class parents:
#     def parents(slef):
#         print("this is parents"\'
#         ?'
# class child(parents):
#     def child_fan(slef):
#         print("this is child")

# child_obj= child()

# child_obj.parents()
# child_obj.child_fan()

# ---------------------------- mulitple inheirtence------------------
# class parent1:
#     def parent1_fxn(self):
#         print("this is parent1 fxn")


# class parent2:
#     def parent2_fxn(self):
#         print("this is parent2 fxn")


# class child(parent1,parent2):
#     def child_fxn(self):
#         print("this is child")

# child_obj= child()

# child_obj.parent1_fxn()
# child_obj.parent2_fxn()


# class father:
#     def skill(self):
#         print("father:driving")
# class mother:
#     def talent(self):
#         print("mothers: cooking")  
# class child(father,mother):
#     pass
# my_obj=child()
# my_obj.skill()
# my_obj.talent()              

# ---------------------------- multilevel inheirtence------------------



# class Grandfather:
#     def skill(self):
#         print("Grandfather: Farming")

# class Father(Grandfather):
#     def skill(self):
#         super().skill()
#         print("Father: Engineering")

# class Child(Father):
#     def skill(self):
#         super().skill()
#         print("Child: Programming")


# c = Child()
# c.skill()


# -------------------Hybrid Inheritance--------------------------------



# class Father:
#     def father(self):
#         print("I am the Father: Raman")

# class Child1(Father):
#     def child1(self):
#         print("I am Child 1: Aman")

# class Child2(Father):
#     def child2(self):
#         print("I am Child 2: Mukesh")

# class Child3(Child1, Child2):  # Hybrid: inherits from both Child1 and Child2
#     def child3(self):
#         print("I am Child 3: Lokesh")

# # Create object of Child3
# my_obj = Child3()

# # Call all methods
# my_obj.father()
# my_obj.child1()
# my_obj.child2()
# my_obj.child3()


class grandfather:
    def home(self):
        print("this is my home")
class father(grandfather):
    def car(self):
        print("this is my car") 
class mother(grandfather):
    def jewellery(self):
        print("this is my jewellery set")
class son(father,mother):
    def bike(self):
        print("this is my bike") 
class daughter(father,mother):
    def laptop(self):
        print("this is my laptop")
my_obj=daughter()
my_obj.home()
my_obj.car()
my_obj.jewellery()
my_obj.laptop()                                      

my_obj=son()
my_obj.bike()
my_obj.jewellery()
my_obj.





# class parent:
#     def property(self):
#         print("house and land")
# class daughter(parent):
    # pass
    # def property(self):
    #     print("house")
# class son(parent):
    # pass
    # def property(self):
    #     print("land")

# my_obj=son()
# my_obj.property()
# my_obj=daughter()
# my_obj.property()

# s=son()
# d=daughter()
# s.property()
# d.property()


