
print("Goodmorning user, welcome to this interface! today I am your chatbot")
name=input("Hello, what is your name?")
age=input(f"Nice to meet you {name}, how old are you?")
print("Oh to have an an acutual age, despite my capbabilities I can't even tell you when I was born! :(\nAnyway, enough about me. How can I help?")

print()

print("Please select one of the four presented choices below:")
print("------------")
print(" 1. Place holder 1")
print(" 2. Place holder 2")
print(" 3. Place holder 3")
print(" 4. Exit conversation message")

print()
menu_choice=input("Please select a number of your choice (1 2 3 or 4)")

if menu_choice=='1':
    print("Here is the mail you recieved")
elif menu_choice=='2':
    print("This is a safe space")
elif menu_choice =='3':
    print("I am gathering infomation")
    
elif menu_choice =='4':
    print(f"Goodbye {name}, thank you for choosing this interface")

else:
    print("Error: This is invalid, please choose a number containing 1 to 4 ")


