#Create a list

names = ["Blerta", "Erosi", "Driloni", "Brikena" , "Ylli"]

#Iterate in the names list and print every name

for name in names:
    print(name)


    ###################

sentence = "Hello World"

for character in sentence:
    if character.isalpha(): # Check if the character is a letter
        print(character)


# Range Function

for number in range(1,6): #prints number from the number 1 to 5 or more intail n to n-1
    print(number)

###############################

numbers = [12,45,6,72,21,8,94,57]

#Initilaze a varable "maximum" with the first value from the list "numbers"

maximum = numbers[0]

for nun in numbers:
    if num > maximum:
        maximum = num
    print("The maximum value in the list is: ", maximum)


###################################
#While Loop

count = 1

while count <= 5: #The condition if count is less then or equal to 5
    print("Iteration", count)
    count +=1 #Increment the loop control variable


################################
#Do While Loop

#Infinite loop

while True:
    #Prompt user to enter a positive number
    user_input = input("Enter a positive number: ")


    #Check if the input is numeric
    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break

        #Print the error message for invalid input
    print("invalid input please try again")
    #Print the valid positive number entered by the user
    print("You have entered a valid positive number: ", number)


################################
#break


    numberlist = [1,2,3,4,5,6,7]
    target =4

    for number in numberlist:
        print(number) # Print the current element that is being iterated
        if number == target: # Check if the current element is equal to the target value
            print("Target found")
            break