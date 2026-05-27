print("Welcome to the. brooklyn 99 quiz")
list_ques=["Who plays the lovable, goofball lead detective?","What is Charles Boyle's favorite holiday, which he refers to as Turkey Day?","What is Captain Raymond Holt's beloved dog named?","What 1988 action film inspired Detective Jake Peralta to become a cop?","Terry Jeffords has a famous addiction to which fruity, frozen treat?","What office supply item does Amy Santiago obsess over and collect?","Who is Jake Peralta's arch-nemesis, a famous and charming car thief?","What is the unusual name of Jake and Amy’s baby boy?"]
list_ans=["jake peralta","thanksgiving","cheddar","die hard","yogurt","binders","doug judy","mac"]
i=0
score=0
for el in list_ques:
    print(el)
    ans=input("your answer").lower()
    if ans==list_ans[i]:
        print("correct answer")
        score+=1
    else:
        print("wrong answer")
    i+=1
    
print("Thanks for taking the quiz your final score is:",score)
    