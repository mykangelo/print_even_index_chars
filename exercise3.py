

#create a input function to ask from the user and store in a variable
any_word = str(input("Please enter any word: "))

#measure the length of the string given from the user
len(any_word)

#print the original string character from the user and the task to print only the even index characters
print("Original String is" , any_word)
print("Printing only even index chars")

#create a for loop and iterate it to the given string from the user
for i in range(0, len(any_word) , 2):        #set the range to find the even index strings from the user
    print(any_word[i])      #use the iteration with the string variable from the user to print only the even index strigns