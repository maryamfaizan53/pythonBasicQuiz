# `#Question 1
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

# You should use the three constants:

# PROMPT JOKE SORRY

# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

# Your program will need to use an if statement which checks if the user input is Joke:

# if user_input == "Joke":

# Recall that == is a comparison which tests if two values are equal to one another.

# Here is a full run of the program (user input is in blue):

# What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'
# Prompt = "what do you want? A joke? yes or no "
# Joke = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
# Sorry = "I only tell jokes"
# user_input = input(Prompt)
# if user_input == "yes":
#     print(Joke)

# else:
#     print(Sorry)



# #question 2
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

# Note that:

# 2 doubled is 4

# 4 doubled is 8

# 8 doubled is 16

# and so on.

# We stop at 128 because that value is greater than 100.

# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

# while curr_value < 100:

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution


# def main():
#         user_input = int(input("Enter a number:"))
#         current_value = user_input*2
#         while current_value <= 100:
#          print(current_value)
#          current_value = current_value * 2

# if __name__ == '__main__':
#     main()








# #question 3
# ## Problem Statement

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Here's a sample run of the program:

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Liftoff!

# def main():
#  for i in range(10, 0, -1):
#     print(i)
#  print("liftoff!") 

# if __name__ == "__main__":
#  main()



# #QUESTION 4
# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# import random

# def main():
#     # Generate the secret number at random!
#     secret_number: int = random.randint(1, 99)
    
#     print("I am thinking of a number between 1 and 99...")
    
#     # Get user's guess
#     guess = int(input("Enter a guess: "))
#     # True if guess is not equal to secret number
#     while guess != secret_number:
#         if guess < secret_number:  # If-statement is True if guess is less than secret number
#             print("Your guess is too low")
#         else:
#             print("Your guess is too high")
            
#         print() # Print an empty line to tidy up the console for new guesses
#         guess: int = int(input("Enter a new guess: "))  # Get a new guess from the user
        
#     print("Congrats! The number was: " + str(secret_number))
    
# if __name__ == '__main__':
#     main()
# import random
# def main():
#         secret_number = random.randint(1, 99)
#         print("I am thinking of a number between 1 and 99...")
#         user_input = int(input("Enter a guess: "))
#         while user_input != secret_number:
#             if user_input < secret_number:
#                 print("Your guess is too low")
#             else:
#                 print("Your guess is too high")    
#             print()   
#             user_input = int(input("Enter a new guess: ")) 
#         print("Congrats! The number was: " + str(secret_number))   

# if __name__ == '__main__':
#     main()






#     Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

# Starter Code
# import random

# N_NUMBERS: int = 10
# MIN_VALUE: int = 1
# MAX_VALUE: int = 100

# def main():
#     """
#     You should write your code here. Make sure to delete 
#     the 'pass' line before starting to write your own code.
#     """
#     pass

# if __name__ == '__main__':
#     main()
# 