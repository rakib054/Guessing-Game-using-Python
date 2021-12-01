import random	#We will select a number using random module

Random_number=random.randint(0,50)

#You can try for 1p times
Try_number=10

print('Hello friends!Welcome to our Guessing Game.You have 10 life.If you can guess number in this life,then you will will.Otherwise,you will lose.')

#Input
Guess_number=int(input('Guess The Number :'))

#Loop 
while True:
    #You can get chance to guess the number correctly. 
    if Guess_number>Random_number+15 :
        print('Your Number is too big')
        Try_number -= 1
        print(f'You have only {Try_number} life left')     
        Guess_number=int(input('Guess The Number :'))
    
    #Can't guess,use that hint
    elif Guess_number>Random_number:
        print('Bigger than actual number')
        Try_number -= 1
        print(f'You have only {Try_number} life left')
        Guess_number=int(input('Guess The Number :'))
   
    #You can do it...
    elif Guess_number<Random_number-15:
         print('Your number is too Small')
         Try_number -= 1
         print(f'You have only {Try_number} life left')
         Guess_number=int(input('Guess The Number :'))
    
    #More hint,more chance of winning          
    elif Guess_number<Random_number:
        print('Smaller than actual number')
        Try_number -= 1
        print(f'You have only {Try_number} life left')
        Guess_number=int(input('Guess The Number :'))

     #Hurray!You did it   
    elif Guess_number==Random_number:
        print('Congrats!You have Guess Correct')
        break
 
    #Alas! You lose       
    if Try_number<2:
        print('You Have Lost')
        break
