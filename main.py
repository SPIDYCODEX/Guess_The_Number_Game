import random
n=random.randint(1,100)

a=-1
Guesses=0
while a!=n:
    a=int(input("Enter the your Guess:"))
    if a<n:
        print("Higher Number Please")
        
    elif a>n:
        print("Lower Number Please")
    Guesses+=1
print(f"You Guess {n} perfect at {Guesses} Guesses")


# Using For Loops For Guess The Number Game:

# import random
# n=random.randint(1,100)
# Guesses=0
# # while True:
# for a in range(1,101):
#     Guesses+=1
#     a =int (input("Guess The Number:"))
#     if a==n:
#       print(f':- 🥂You Guesses the Exact Number ({a}) in {Guesses} attempt🙌')
#     elif a<n:
#       print("Guess Higher Number⏫")
#     elif a>n:
#       print("Guess Lesser Number⏬")
    
# print("Thank You For Your Guess🙏🏾")