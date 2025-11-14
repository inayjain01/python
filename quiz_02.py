#Ques 1: What is the value of y after this code runs?
x = 10
y = x * 2 - 5
print(y)
# Answer: 15

# Ques 2: What does this code print?
word = "Python"
print(word[0] + word[-1])
# Answer: Pn

# Ques 3: How many times will this print "Hi"?
for i in range(2, 7):
    print("Hi")
# Answer: 5 times

# Ques 4: What does this code print?
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# Answer: banana

# Ques 5: What will this print?
number = 8
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# Answer: Even

# Ques 6: Write a short Python program that asks for your favorite color and prints:
# "Your favorite color is COLOR!"
# (replace COLOR with what the user types)
color = input("What is your favorite color? ")
print("Your favorite color is " + color + "!")

# Ques 7: What does this print?
for i in range(3):
    print(i * 2)
# Answer: 0 2 4

# Ques 8: Write a function to multiply 5 differnt numbers and return the result
def multiply_five_numbers(a, b, c, d, e):
    return a * b * c * d * e

# Example usage:
result = multiply_five_numbers(2, 3, 4, 1, 5)
print(result)  
# Answer: 120
