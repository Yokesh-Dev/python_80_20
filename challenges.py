# 1
num1 = 15
num2 = 13

print(num1 + num2)   
print(num1 - num2)  
print(num1 * num2)   
print(num1 / num2)   

# 2
user_year = int(input("Enter your year of birth: "))
current_year = 2026
user_age = current_year - user_year

print("You are", user_age, "years old.")


# 1
num = 12
floatnum = 11.3
name = "str"
status = True

print(num, type(num))
print(floatnum, type(floatnum))
print(name, type(name))
print(status, type(status))

# 2 
user_input = int(input("Enter a Number "))
user_input2 = int(input("Enter another Number "))

print(user_input + user_input2 , user_input2 * user_input)

# 3
lists = [11,12,23,24]
lists.append(25)
print(lists , len(lists))
lists.remove(11)
print(lists , len(lists))
