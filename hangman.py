# Code Alpha Project 1- Hangman Game
import random

#lists that will be select randomly 
fruits=["mango","banana","papaya", "Orange", "lemon","kiwi","watermelon","Berry"]
sports=["cricket","football","hocky","baseball","basketball","boxing","badminton"]
smartphones=["Samsung","oppo","realme","iphone","oneplus","xaomi","vivo","techno","Asus"]
clothBrands=["Zara","Zudio","HM","venhusen","Calvin","Levis","Puma","Rymond"]
Laptops=["Acer","Dell","HP","Lenovo","MSI","Asus"]

lists =[fruits,sports,smartphones,Laptops,clothBrands]
collection=random.choice(lists) #select list


def find(word,guess): #function wich find and store index of correct guessed word
    index_list=[]
    for i ,j in enumerate(word):
        if j==guess:
            index_list.append(i)
    return index_list

def get_name(var): # function that return List name
    for name, value in globals().items():
        if value is var:
            return name
        
name=get_name(collection)

player=input("ENTER YOUR NAME-")
print("welcome ",player,"!")
print("Let's play the hangman game")

# randomly choose a secret word from  LIST.
print("Guess the name from the",name)
word=random.choice(collection)
word=word.upper() #convert word in uppercase

l=len(word) # length of word
lives=3  #lives or max 3 chances to guess wrong
print("you have a maximum",lives,"lives" )
space=['_']*l
print("word is -","_ "*l)

# List for storing the letters guessed by the player
letterGuessed = ''
count = 0
flag = 0 

while(lives != 0 ) and flag==0:  # Flag is updated when the word is correctly guessed

    try:
        print()
        guess = str(input('Enter a letter to guess: '))
    except:
        print('Enter only a letter!')
        continue

    # Validation of the guess
    guess=guess.upper()
    if not guess.isalpha():
        print('Enter only a LETTER')
        continue
       
    elif len(guess)> 1:
        print('Enter only a SINGLE letter')
        continue
    elif guess in letterGuessed:
        print('You have already guessed that letter')
        continue

    # If letter is guessed correctly
    if guess in word:
        char_count=word.count(guess)
        count=count+char_count
        letterGuessed+=guess
        indices=find(word,guess)
        for index in indices:
            space[index]=guess
            words=(" ".join(space))
        print("word is -",words)
    else:
        lives-=1
        print("you gussed wrong !")
    if l==count:
        print(" CONGRACTULATION YOU WON ")
        flag=1
if flag==0:      
  print("oh ! try next time")    