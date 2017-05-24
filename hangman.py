
error1="""
          ______________________
          |                    ___
          |                   |   |
          |                   |_ _|
          |                   
          |                    
          |                 
          |                   
          |                 
          |                
          |                    
          |                    
          |                   
          |                  
          |                 
          |              
          |
________________________
"""
error2="""
          ______________________
          |                    ___
          |                   |   |
          |                   |_ _|
          |                   
          |                    | |
          |                    | |
          |                    | |  
          |                    | |  
          |                
          |                    
          |                    
          |                   
          |                 
          |                 
          |              
          |
________________________
"""
error3="""
          _______________________
          |                    ___
          |                   |   |
          |                   |_ _|
          |                   
          |                    | |
          |                    | |
          |                    | |  
          |                    | |  
          |                    | |   
          |                    | |
          |                    
          |                   
          |                 
          |                 
          |             
          |
________________________
"""
error4="""
          _______________________
          |                    _|_
          |                   |   |
          |                   |_ _|
          |                   
          |                    | |
          |                    | |
          |                    | |  
          |                    | |  
          |                    | |   
          |                    | |
          |                    ---
          |                     
          |                       
          |                      
          |                    
          |
________________________
"""
error5="""
          _______________________
          |                    _|_
          |                   |   |
          |                   |_ _|
          |                     |
          |                    | |
          |                    | |
          |                    | |  
          |                    | |  
          |                    | |   
          |                    | |
          |                    ---
          |                        
          |                        
          |                         
          |                    
          |
________________________
"""
error6="""
          _______________________
          |                    _|_
          |                   |   |
          |                   |_ _|
          |                     |
          |                    | |  
          |                   /| |\  
          |                  / | | \   
          |                 /  | |  \  
          |                o   | |   o  
          |                    | |
          |                    ---
          |                    | |  
          |                    | | 
          |                    | | 
          |                 ___| |___
          |
________________________
"""
words = [
'butterfly',
'spider',
'dog',
'cat',
'monkey',
'tiger',
'lion',
'giraffe',
'gorilla',
'whale',
'polar bear',
'dolphin',
'bear',
'eagle',
'snake',
'fish',
'jackal',
'panther',
'penguin',
'elephant',
'zebra',
'horse',
'panda',
'lizard',
'rhino',
]


word = int(raw_input("Please pick a number 0 through 24, this will decide the word you are going to guess.\n"))
wordd = words[word]
losecount = 6
count=0
print("Welcome to Hangman!")
print("Okay I now have the word that you are going to guess!")
print("The one and only hint I will give you for this entire game is that the word you are trying to guess is an animal of some sort.")
guess=len(wordd)
toprint=""
listof=[]
tempstr=""
for i in range(0,guess,1):
	toprint+="_"
	listof.append("_")
while(count!=losecount and wordd!=tempstr):
	match=False
	letterz=str(raw_input("Now guess a letter!\n"))
	tempstr=""
	for letter in wordd:
		if(letter==letterz):
			match=True
			where=wordd.find(letter)
			tmp=toprint[where]
	if(match==False):
		count+=1
		if(count==1):
			print(error1)
		if(count==2):
			print(error2)
		if(count==3):
			print(error3)
		if(count==4):
			print(error4)
		if(count==5):
			print(error5)
		if(count==6):
			print(error6)
	if(match==True):
		listof[where]=letterz
		for i in listof:
			tempstr=tempstr+i
		print(tempstr)
if(count==losecount):
	print("Aww, you suck at life turd, that's why you are dead.")
if(wordd==tempstr):
	print("Congrats you won, the word was {}.".format(wordd))