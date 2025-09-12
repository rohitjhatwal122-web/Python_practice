# class SBI:
#     bank_account_holder = "ROHIT"
#     bank_account_number = "1112345678"

#     _bank_balance = 8999 
#     __atm_number = "23456"
#     __atm_pass = "123" 



# class Branch1(SBI):
    # pass

# Create object of SBI
# my_obj = SBI()

# print(my_obj.bank_account_holder)     # ✅ Accessible (public)
# print(my_obj.bank_account_number)     # ✅ Accessible (public)
# print(my_obj._bank_balance)           # ⚠️ Accessible (protected, but discouraged)

# print(my_obj.__atm_number)          # ❌ Error: AttributeError
# print(my_obj.__atm_pass)            # ❌ Error: AttributeError

# Create object of Branch1
# branch_obj = Branch1()

# print(branch_obj.__atm_number)      # ❌ Error: AttributeError
# print(branch_obj._bank_balance)


# note: private member can't be accessed , even using inheirtence, within the class we can access it 
# note : protected member can be accessed by inheritence and using obj of that class 



class PNB:
    bank_account_holder = "ROHIT"
    bank_account_number = "1112345678"
    IFSC_Code="123947647"
    Address ="punjab" 
    Date_of_Opening="12-10-2024"
    Type_of_Account="saving account"

    _bank_balance="5032"
    __atm_number="12121212"
    __atm_pass="12005"

class branch1(PNB):
    bank_account_holder = "mohit"
    bank_account_number = "11145678"
    IFSC_Code="123947"
    Address ="Bathinda" 
    Date_of_Opening="12-10-2020"
    Type_of_Account="saving account"

    _bank_balance="23455"
    __atm_number="12234512"
    __atm_pass="8923457"

class branch2(PNB):
          bank_account_holder = "vikash"
          bank_account_number = "1114567348"
          IFSC_Code="1239434347"
          Address ="ganganagar" 
          Date_of_Opening="15-10-2020"
          Type_of_Account="saving account"

          _bank_balance="234455"
          __atm_number="34512"
          __atm_pass="823457"

main_branch = PNB()
my_obj=PNB
print(my_obj.bank_account_holder)
print(my_obj.bank_account_number)
print(my_obj.IFSC_Code)
print(my_obj.Address)
print(my_obj.Date_of_Opening)
print(my_obj.Type_of_Account)
print(my_obj._bank_balance)
# print(my_obj.__atm_number)
# print(my_obj.__atm_pass)

print("\n----------------------\n")

PNB=branch1
my_obj=branch1
print(my_obj.bank_account_holder)
print(my_obj.bank_account_number)
print(my_obj.IFSC_Code)
print(my_obj.Address)
print(my_obj.Date_of_Opening)
print(my_obj.Type_of_Account)
print(my_obj._bank_balance)
print("\n----------------------\n")
PNB=branch2
my_obj=branch2
print(my_obj.bank_account_holder)
print(my_obj.bank_account_number)
print(my_obj.IFSC_Code)
print(my_obj.Address)
print(my_obj.Date_of_Opening)
print(my_obj.Type_of_Account)
print(my_obj._bank_balance)
