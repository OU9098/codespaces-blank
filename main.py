place_holder_1='1'
place_holder_2='2'
place_holder_3='3'
exit_conversation_message='4'

print("Goodmorning user, welcome to this interface! today I am your chatbot")
name=input("Hello, what is your name?")
age=input(f"Nice to meet you {name}, how old are you?")
print("Oh to have an an acutual age, despite my capbabilities I can't even tell you when I was born! :(\nAnyway, enough about me. How can I help?")

print()

print("Please select one of the five presented choices below:")
menu_options=['place holder 1','place holder 2','place holder 3','exit conversation message']
for word in menu_options:
    print ('-' + word)

menu_choice=input("Enter a number you wish to use:")

if menu_choice=='1':
    print("Hello there")
elif menu_choice=='2':
    print("This is a safe space")
elif menu_choice =='3':
    print("Help is on the way")
elif menu_choice =='4':
    print(f"Goodbye {name}, thank you for choosing this interface")

else:
    print("Please choose a number between 1 through 4")




