		importrandom
		
		defguess(x):
		    random_number=random.randint(1, x)
		    guess=0
		    whileguess!=random_number:
		        guess=int(input(f'Guess a number between 1 and {x}: '))
		        ifguess<random_number:
		            print('Sorry, guess again. Too low.')
		        elifguess>random_number:
		            print('Sorry, guess again. Too high.')
		
		    print(f'Yay, congrats. You have guessed the number {random_number}correctly!!')
		
		defcomputer_guess(x):
		    low=1
		    high=x
		    feedback=''
		    whilefeedback!='c':
		        iflow!=high:
		            guess=random.randint(low, high)
		        else:
		            guess=low# could also be high b/c low = high
		        feedback=input(f'Is {guess}too high (H), too low (L), or correct (C)?? ').lower()
		        iffeedback=='h':
		            high=guess-1
		        eliffeedback=='l':
		            low=guess+1
		
		    print(f'Yay! The computer guessed your number, {guess}, correctly!')
		
		
		guess(10)
