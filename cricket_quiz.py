print("Welcome to Quiz game")

print("Do u wanna a play?  ")
playing = input()

if playing.lower() != "yes":
    quit()
else:
    print("come on lets play!")

score = 0

ans = input("who is called as god of cricket?   ")
if ans.lower() == "sachin" or ans.lower() == "sachin tendulkar":
    print("Correct")
    score += 1
else:
    print("Incorrect")

ans = input("which country has the world cup most times?  ")
if ans.lower() == "aus" or ans.lower() == "australia":
    print("correct")
    score += 1
else:
    print("Incorrect")

ans = input("who was the man of the tournament in 2011 world cup?  ")
if ans.lower() == "yuvraj singh":
    print("correct")
    score += 1
else:
    print("Incorrect")

ans = input("who has  scored the most number of runs in single edition of IPL season?  ")
if ans.lower() == "virat" or ans.lower() == "virat kholi":
    print("correct")
    score += 1
else:
    print("Incorrect")
ans = input("which captain has all the major trophies conducted by ICC?  ")
if ans.lower() == "msd" or ans.lower() == "dhoni":
    print("correct")
    score += 1
else:
    print("Incorrect")

print("you have got  " + str(score) + "  correct")
print("you have secured  "+str((score/5)*100)+"  %")
