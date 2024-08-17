import random

n = random.randint(1,100)
print(n)

a = 0
guesses = 0

while(a !=n):
    a = int(input("Guess the number"))
    if(a>n):
        print("lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1
        
print(f"you have guessed thr correct number that is {n} in {guesses} attempts")            