# -------------------------Arithmetic--------------------------------------

# a=30
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)


# ----------------------------logical--------------------------------------------
# a=10
# b=20
# print(a<b and b>a)


# print(a<b or a>b)

# print(not(a<b and b>a))


# ------------------------------bitwise---------------------

# a=10
# b=20
# print(a & b)


# print(a | b)

# print(~a)
# print(~b)


# ---------------------assigmeent-----------------------------------

# a=10
# b=20
# a=a+10
# print(a+b)

# a=a-5
# print(a+b)


# =-----------------------------membership-------------------------

# lang="python"
# print("y" in lang)
# print("z" in lang)
# print("z" not in lang)

# -------------------------identy------------------------------------
# a=[10,20,30]
# b=[10,20,30]
# print(a is b)
# print(a is not b)
# b=a
# print(a is b)

# --------------------------input fxn------------------
# a=int(input("enter your valu, a: "))
# b=int(input("enter your value, b:"))
# print(a+b)


# -----------------------string method-----------------------

# lang="programming"
# x=lang.capitalize()
# print(x)

# y=lang.upper()
# print(y)
 
# z=lang.lower()
# print(z)

# a=lang.title()
# print(a)

# b=lang.count('m')
# print(b)

# c=lang.startswith('p')
# print(c)

# d=lang.endswith('g')
# print(d)

# e=lang.find('n')
# print(e)

# f=lang.index(5)
# print(f)

# lang="     hello    "
# g=lang.strip()
# print(g)

# txt = "welcome to my world "
# h=txt.replace("to", "and")
# print(h)

# ---------------------------------------string slicing---------------------
# lang="programming"
# print(lang[:])
# print(lang[:9])
# print(lang[3:9])
# print(lang[::-1])
# print(lang[-1::])
# print(lang[-5:-1])

# -----------------------------------------list-----------------------------------------

# listt1=["rohit", 2.3, "gagan"]
# print(listt1)

# listt2=[12,13,14,15,16,17]
# listt2[5]=786
# print(listt2)

# -----------------------list method -------------------------

# txt=[1,2,4,5,6,7,8]
# txt.append(55)
# print(txt)

# txt=[1,2,3,4]
# txt.extend([23,24,12])
# print(txt)

# txt2=[22,33,44]
# txt2.remove(22)
# print(txt2)

# txt3=[22,33,44,55,66,77,88,99]
# txt3.clear()
# print()

# txt4=[22,33,44,55,66,77,88,99]
# txt4.pop()
# print(txt4)


# txt5=[22,33,44,55,123,234,453]
# txt5.sort()
# print(txt5)

# txt6=[22,33,44,55,22,33,22,32,22,123,234,453]
# print(txt6.count(22))

# txt7=[12,"apple",22,33,44]
# txt7.insert(3, "mango")
# print(txt7)

# -------------------while loop-------------------------------
# i=0
# while (i<5):
#     print(i)
#     i=i+1

# i=0
# while (i<10):
#     print(i)
#     i=i+1


# --------------------------for loop---------------------------------
# for i in range(2):
#     for j in range(3):
#         print(i,j)


# for i in range(2):
#     print(i)

# print("u\tv")
# for u in range(3):
#     for v in range(7):
#         print(f"{u}\t{v}")


# -----------------------funcation--------------------------------
# def rohit():
#     print("this is rohit")

# rohit()
# rohit()

# def sum(a,b):
#     print(a+b)
# sum(20,30)    



# def sum(a,b=20):
#     print(a+b)

# sum(45)
# sum(20,30)

# --------------------------------conditional stmmt------------------------------------------
# x=10
# y=20
# if x<y:
#     print("y is greater")


# x=12
# y=6
# if (x>y and y<x):
#     print("x is greater")
# else:
#     print("y is greater")

# age=int(input("enter your age"))
# if age>=18:
#     print("The candidate is eligible to vote.")
# else:
#     print("The candidate not is eligible to vote.")    

# def chek_even_odd(x):
#     if x%2==0:
#         print("even number")
#     else:
#         print("odd number") 
# # chek_even_odd(50)
# x=int(input("enter your value"))



# ---------------------------------brack & continue=---------------------

# for i in range(6):
#     if (i==3):
#         break
#     print(i)   


# for i in range(6):
    # if (i==4):
    #     continue
    # print(i)  

# ---------------------------------------predifind ----------------------

# listt=[1,2,3,4,23,24,78,56,345]
# print(max(listt))

# print(min(listt))

# print(sum(listt))

# print(sorted(listt))

# ---------------------------oops---------------------
# ---------------global variable------------------------
# x=5
# print(x)
# def myfxn():
#     print(x)

# myfxn()    

# -------------------------local variable---------------------
# x=10
# print(x)
# def my_fxn():
#     y=20
#     print(y)
# my_fxn()
# print(y)

# -------------------------------------------------------------------------------------
# class myclass:
#     def my_fxn():
#         print("this is my_fxn")

# my_boj=myclass
# my_boj.my_fxn()

# ----------------------------inheritense------------------------
# class parent:
#     name="rohit"
#     def first():
#         print("this is first class")
# my_obj=parent
# print(my_obj.name)    
# my_obj.first()

# class parent:
#     def parent(self):
#         print("this is parent")

# class child(parent):
#     def child_fxn(self): 
#      print("this is child")

# child_obj=child()
# child_obj.parent()
# child_obj.child_fxn()

# class language:
#     def programming(self):
#         print("this is php")
# class lang2(language):
#     def programming(self):
#         print("this is python")
# class lang3(language):
#     def programming(self):
#         print("this is java") 

# my_obj=language()
# my_obj.programming()
# my_obj=lang2()
# my_obj.programming()
# my_obj=lang3()
# my_obj.programming()



#  ------------------------------------"Encapsulation------------------------

# class SBI:
#     account_holder_name="rohit kumar"
#     account_nuber="2397547595739"
#     account_ifcs_code="35768358635"
#     _bank_balance="20000"
#     __atm_number="8439"
#     __atm_password="2003"

# class branch1(SBI):
#     account_holder_name="mohit kumar"
#     account_nuber="239757777739"
#     account_ifcs_code="353454358635"
#     _bank_balance="20300"
#     __atm_number="8423"
#     __atm_password="2053"

# bank_obj=SBI()
# print(bank_obj.account_holder_name)    
# print(bank_obj.account_nuber)
# print(bank_obj.account_ifcs_code)
# print(bank_obj._bank_balance)
# # print(bank_obj.__atm_number)
# # print(bank_obj.__atm_password)
# print()


        


# --------------------------prime no-------------------------

x = 5

is_prime = True


for i in range(2, x):
    if (x % i == 0):
        is_prime = False
        break
    
if is_prime:
    print("this is prime number")
else:
    print("this is non prime")


























































# def check_palindrome():
#    s=input("enter your name:").lower()
#    if  s == s[::-1]:
#         print("name is a palindrome")
#    else:
#         print("name is not a polindrome")   
# check_palindrome()     



# num=int(input("enter your valu"))
# if num >0:
#     print("positive")
# elif num <0:
#     print("negative")
# else:
#     print("zero")

# x=int(input("enter your number:"))
# def check_even_odd():
#     if x%2==0:
#         print("this number is even")
#     else:
#         print("this number is odd")    

# check_even_odd()


