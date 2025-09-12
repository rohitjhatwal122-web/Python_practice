class bank:
    
    name="SBI"
    def first(self):
        print("this first branch SBI jaipur")
        print("branch name is ", self.name) 
    def secoend(self):
        print("this secoend branch SBI kikarwali") 
    def third(self):
        print("this third branch SBI raisinghnagar") 

my_obj = bank()
print(my_obj.name)

print(my_obj.first())