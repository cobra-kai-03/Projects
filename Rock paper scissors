		import random
		def play():
		    user=input("Whats your choice r, s, p")
		    computer=random.choice(['r','s','p'])
		    if user == computer:
		        return 'tie'
		    if iswin(user,computer):
		        return 'You won'
		        
		    return 'You lose'
		#s>p,p>r,r>s
		def iswin(player,opponent):
		    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's'):
		        return True
		    
print(play())
