from datetime import datetime
# section one
name = "Karla"
age = 43
height = 5.6
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# section two
name = input("Please enter your name: ")
current_year = datetime.now().year
year_born = input("Please enter the year you were born: ")
year_born =int(year_born)
#subtract year_born from current_year to find age
age = current_year - year_born

#todays_age = age - int(year_born)
print("Hi,",name,"! You are approximately", age," years old.")

#section three
num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a second number: "))
multiplied = num1*num2
print(f"{num1} x {num2} = {multiplied}")

#test with lines
item = "Java Script Book"
qty = 3
price = 12.35
total = int(qty)*price

print("----------------------------------")
print('             RECEIPT              ')
print("----------------------------------")

print("Item: ", item.rjust(20))
print("Quantity: ",str(qty).ljust(10) )
print("Price: ",f"{price:8.2f}") 
print("----------------------------------")
print("Total: ",f"{total:8.2f}")
print("----------------------------------")

#section five
name = input("Please enter your name: ")
hometown = input("What is your hometown: ")
hobby = input("What is your favorite hobby: ")
fun_fact = input("Please enter a fun fact about you: ")
year_born = int(input("What year were you born: "))
#year_born =int(year_born)
current_year = datetime.now().year
age = current_year - year_born

print(" ")
print("================================")
print("                                ")
print("     PROFILE:", name             )          
print("                                ")
print("================================")
print(f"Hometown: {hometown.rjust(10)}")
print(f"Hobby: {hobby.rjust(19)}")
print(f"Fun fact: {fun_fact.rjust(22)}")
print(f"Age: {str(age).rjust(10)}")
print("================================")
