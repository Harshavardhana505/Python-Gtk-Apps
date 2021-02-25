prompt1=input('Can I make this stupid thing work?')   
while True: 
	prompt1=input('Can I make this stupid thing work?').lower() 
	if prompt1 == 'yes': print('Hooray, I can!') 
	if prompt1 == 'no': print('Well I did anyway!')
else: print('Huh?')
