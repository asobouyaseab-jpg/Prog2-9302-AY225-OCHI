password = "select"
for attempt in range(3):
    guess = input("enter password: ")
    if guess == password:
        print("Access granted!") 
        break
    else:
        print("Wrong password!")
else:
    print("Too many wrong tries. program terminated.")