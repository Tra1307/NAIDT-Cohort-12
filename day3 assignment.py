#True love calculator

print("This is a true love calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()
name = name1 + name2
print(name)
true_word  = "true"
love_word = "love"

true_count = 0
love_count = 0

for true in true_word:
    true_count += name.count(true)

for love in love_word:
    love_count += name.count(love)

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your Score is {love_score}%, you go together like coke and menthos!")

elif love_score >= 40 and love_score <= 50:
    print(f"Your Score is {love_score}%, you are alright together!")

else:
    print(f"your score is {love_score}%")