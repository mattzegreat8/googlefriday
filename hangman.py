import hangmanpic
import wordlist

word = int(raw_input("Please pick a number 0 through 24, this will decide the word you are going to guess."))
wordd = wordlist.words[word]
losecount = 6
count=0
print("Welcome to Hangman!")
print("Okay I now have the word that you are going to guess!")
print("The one and only hint I will give you for this entire game is that the word you are trying to guess is an animal of some sort.")
print(len(wordlist.words[word]))
print("That number is how many charecters are in the word you picked")


while(count != losecount):
	guess= raw_input("please guess a letter"'>')

	if(len(guess)!= 1):
		print("please only input one charecter to guess")
		guess= raw_input("please guess a letter"'>')
	if(guess in wordd):
		print("Good job! That letter is in the word you are guessing.")

	if(guess not in wordd):
		print("I am sorry but that letter is not in the word!")
		count +=1
	for letter in wordd:
		if(guess in wordd):
			print(guess)
			print("_")
		elif(guess not in wordd):
			print("_")

	if(count == losecount):
		print("I am sorry but you lost the game.")
#print(hangmanpic.body)
#print (wordlist.words[0])
#print(wordlist.words[word])