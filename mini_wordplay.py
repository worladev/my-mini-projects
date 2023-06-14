import io
from string import punctuation

# SOLUTION
sentence = "Wow, his father bought him the prettiest car of them all."

try:
    my_file = open('txtFiles/words.txt')
except:
    print("Could not find your file")

list_of_words = ["wow", "start", "tags", "madam", "racecar", "love", "man", "pot"]


class Wordplay:
    def __init__(self, words_input):
        #self.words = words
    ## {Some Modifications Here.}
        if isinstance(words_input, str):
            for punc in punctuation:
                words_input = words_input.replace(punc, "")
            self.words = words_input.lower().split()

        elif isinstance(words_input, io.TextIOBase):
            self.words = [word.strip() for word in words_input]

        elif isinstance(words_input, list):
            self.words = words_input
    ## {Some Modifications Here.}

    # returns a list of all the words of length (length)
    def words_with_length(self, length):
        output_list = [word for word in self.words if len(word) == length]
        return output_list
    
    # returns a list of all the words that start with (char)
    def starts_with(self, char):
        output = []
        # output_list = [word for word in self.words if word[:len(char)] == char]
        # return output_list
        for word in self.words:
            if word[0] == char:
                output.append(word)
        return output
    
    # returns a list of all the words that end with (char)
    def ends_with(self, char):
        output_list = []
        # output_list = [word for word in self.words if word[-len(char):] == char]
        for word in self.words:
            if word[-1] == char:
                output_list.append(word)
        return output_list
    

    # returns a list of all the palindromes in the list
    def palindromes(self):
        ## {Some Modifications Here.}
        pali_output = []
        # pali_output = [word for word in self.words if word[::-1] == word]
        for word in self.words:
            if word == word[::-1]:
                pali_output.append(word)
        return pali_output
    
    
    # returns a list of the words that contain only those letters in (letter)
    def only(self, letter):
        # output_list = [word for word in self.words if letter.lower() in word]
        output_list = []
        for word in self.words:
            if letter in word:
                output_list.append(word)
        return output_list
    

    # returns a list of the words that contain none of the letters in (letter)
    def avoids(self, letter):
        # output_list = [word for word in self.words if letter.lower() not in word]
        output_list = []
        for word in self.words:
            if letter not in word:
                output_list.append(word)
        return output_list

    
wordclass = Wordplay(list_of_words)
# wordclass2 = Wordplay(sentence)
# wordclass3 = Wordplay(my_file)

# print(wordclass.words_with_length(5))
# print(wordclass.starts_with("m"))
# print(wordclass.ends_with("t"))
# print(wordclass.palindromes())
# print(wordclass.only("o"))
# print(wordclass.avoids("AR"))








'''
QUESTION

Write a class called Wordplay.
It should have a field that holds a list of words. 
The user of the class should pass the list of words they want to use to the class. 
There should be the following methods:
    • words_with_length(length) — returns a list of all the words of length length
    • starts_with(s) — returns a list of all the words that start with s
    • ends_with(s) — returns a list of all the words that end with s
    • palindromes() — returns a list of all the palindromes in the list
    • only(L) — returns a list of the words that contain only those letters in L
    • avoids(L) — returns a list of the words that contain none of the letters in L

wow, racecar, madam

Use Case
wordplay = WordPlay([racecar, boy , girls, children, toy, redolf, try, top, madam, civic])
wordplay.words_with_length(3)
wordplay.starts_with(t)
wordplay.ends_with(y)
'''