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



#1 
lists = [1,2,3,4,5]
print(lists[0] , lists[4])


#2 
dicty ={"name" :"Moses", "age":12 , "city":"Russia" }
dicty["age"]= 17

print(dicty)

# 3
lists =[1,2,3,4,5,5,6,7,8,8,7,6]
print(lists)
filters_lists= sorted(set(lists))
print(filters_lists)

---
#1 
num = 4

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2 
for i in range(1,11) :
    if(i  %2 ==0) :
         print(i)

#3

---
#1 
def greet():
    user_input=input("Enter Your Name: ")
    print(f"Welcome {user_input}  to the Page ")
    
greet()

#2

