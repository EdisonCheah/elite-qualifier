import time
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words
  
def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that

  if " " in text: #Checks if the user's input is a sentence
    split_sentence = text.split() #Split sentence into word
    for word in split_sentence:
      if word.lower() in all_words: #If word is in dictionary
        print(word + ' is a word. Would you like to see the definition for it?')
        text3 = input(':> ')
        if text3.lower() == 'yes':
          print(dictionary.meaning(word)) #Prints definition of word
        else:
          pass
      else: #If word is not in dictionary
        char_list = list(word)
        with open('safedict_simple.txt', 'r') as f:
          for line in f:
            x = 0
            common_chars = 0
            suggest_words = []

            char2_list = list(line) #Converts each word in .txt file into individual characters
            for char in char_list:  #Compares characters from user input word and each word in the .txt file
              if char == char2_list[x]:
                x+=1
                common_chars+=1
              else:
                break
            if common_chars >=3:
              suggest_words.append(line)  #Appends words with >=3 identical characters to user's word
              print(word + ' is not a word. Did you mean:')
              for word in suggest_words:
                print(word)
              text2 = input(':> ')
              if text2.lower() == 'yes':
                print('Success!')
                break
              elif text2.lower() == 'no':
                print("That's okay!")
                continue
          if len(suggest_words) == 0: #If no similar words found
            print("Sorry! No words found. Please enter another word")

  else: #If user's input is an individual word
    if text.lower() in all_words: #If word is in dictionary
      print(text + ' is a word. Would you like to see the definition for it?')
      text3 = input(':> ')
      if text3.lower() == 'yes':
        print(dictionary.meaning(text)) #Prints definition of word
      else:
        pass
    else: #If word is not in dictionary
      char_list = list(text)
      with open('safedict_simple.txt', 'r') as f:
        for line in f:
          x = 0
          common_chars = 0
          suggest_words = []

          char2_list = list(line) #Converts each word in .txt file into individual characters
          for char in char_list:  #Compares characters from user input word and each word in the .txt file
            if char == char2_list[x]:
              x+=1
              common_chars+=1
            else:
              break
          if common_chars >=3:
            suggest_words.append(line)  #Appends words with >=3 identical characters to user's word
            print(text + ' is not a word. Did you mean:')
            for word in suggest_words:
              print(word)
            text2 = input(':> ')
            if text2.lower() == 'yes':
              print('Success!')
              break
            elif text2.lower() == 'no':
              print("That's okay!")
              continue
        if len(suggest_words) == 0: #If no similar words found
          print("Sorry! No words found. Please enter another word")
    #print(text + ' is not a word')

def main():
    all_words = load_words()
    print('Type some text, or type \"/quit\" to stop')
    while True:
        text = input(':> ')
        if ('/quit' == text):
          print('Okay, goodbye')
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

