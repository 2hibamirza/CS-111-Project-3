# CS 111 Project 3
# Hawaiian Word Pronunciation

# Prompt user to input a hawaiian word
# Give user a pronunciation of the hawaiian word

# Name: Hiba Mirza

CONSONANTS = {
  'p',
  'k',
  'h',
  'l',
  'm',
  'n',
  'w'
}
VOWEL_PRONUNCIATIONS = {
  'a':'ah',
  'e':'eh',
  'i':'ee',
  'o':'oh',
  'u':'oo'
}
VOWEL_PAIRS = {
  'ai':'eye',
  'ae':'eye',
  'ao':'ow',
  'au':'ow',
  'ei':'ay',
  'eu':'eh-oo',
  'iu':'ew',
  'oi':'oy',
  'ou':'ow',
  'ui':'ooey'
}

# for handling 'w'
WSOUND = ('a', 'u', 'o')
VSOUND = ('i', 'e')

# choices the user can input
yes_choices = ['y','yes','YES']
no_choices = ['n','no','NO']

# boolean for loop
restart = True

while restart == True:
  i = 0
  # get user input
  word = input("Enter a hawaiian word: ")
  word = word.lower()
  pronunciation = ''
  while i < (len(word)):
    letter = word[i]
    # handle non-vowels
    if letter in CONSONANTS:
      # handle w
      if letter == 'w':
        # if w is the first letter keep it the same
        if i == 0:
          pronunciation += letter
        else:
          previousLetter = word[i-1]
          if previousLetter in WSOUND:
            # keep the letter as a 'w'
            pronunciation += letter
          # if the word before is an 'i' or 'e', replace the 'w' with a 'v'
          elif previousLetter in VSOUND:
            pronunciation += 'v'  
      # non-w
      else:
        pronunciation += letter
    # vowels
    elif letter in VOWEL_PRONUNCIATIONS:
      # last letter?
      if i < len(word)-1:
        next_letter = word[i+1]
      else:
        next_letter = ''

      # check for vowel pairs
      pair = letter + next_letter
      if pair in VOWEL_PAIRS:
        if i+1 == len(word)-1 or (word[i+2] == ' ') :
          pronunciation += VOWEL_PAIRS[pair]
        else:
          pronunciation += VOWEL_PAIRS[pair] + '-'
        # skip the next vowel since it's a valid pair
        i += 1
      elif (next_letter == "'") or (next_letter == ' '):
        pronunciation += VOWEL_PRONUNCIATIONS[letter]
      elif (next_letter == '') :
        # not a valid vowel pair, treat as single vowel
        pronunciation += VOWEL_PRONUNCIATIONS[letter] 
      else:
        pronunciation += VOWEL_PRONUNCIATIONS[letter] +'-'
    # keep apostrophe
    elif letter == "'":
      pronunciation+= "'"
    elif letter == " ":
      pronunciation+= " "
    # invalid letter
    else:
      pronunciation = 'invalid'
      # stop loop by forcing condition to be false
      i = len(word)
    # increment counter
    i += 1

  if pronunciation == 'invalid':
    print("Invalid word, " + letter + " is not a valid hawaiian character.")
  else:
    # remove trailing hyphen if one exists
    pronunciation = pronunciation[0].upper() + pronunciation[1:]
    print(word.upper() + " is pronounced " + pronunciation)

  # ask user if they would like to enter another word
  answer = input("Would you like to enter another word? [y/yes, n/no] ")
  answer = answer.lower()
  # answer will handle whether the loop will run again or not
  if answer in yes_choices:
    restart = True
  if answer in no_choices:
    restart = False

# loop will not run
if restart == False:
  print("All done.")