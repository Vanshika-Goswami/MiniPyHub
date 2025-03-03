#password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','U','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['`','~','!','@','#','$','%','^','&','*',')','(','-','_','+','=',']','[','}','{',':',';','<','>','?','|']
print("Welcome to the PyPassword Generator")
length_letter=int(input("How many letters would you like in your password?\n"))
length_symbol=int(input("How many symbols would you like in your password?\n"))
length_numbers=int(input("How many numbers would you like in your password?\n"))
# Easy
# password=""
# for char in range(1,length_letter+1):
#     password=password+random.choice(letters)
# for char in range(1,length_symbol+1):
#     password=password+random.choice(symbols)
# for char in range(1,length_numbers+1):
#     password=password+random.choice(numbers)

# print("Here is your password:",password)

password_list=[]
for char in range(1,length_letter+1):
    password_list+=random.choice(letters)
for char in range(1,length_symbol+1):
    password_list+=random.choice(symbols)
for char in range(1,length_numbers+1):
    password_list+=random.choice(numbers)
random.shuffle(password_list)
password=""
for i in password_list:
    password += i

print("Here is your password:",password)