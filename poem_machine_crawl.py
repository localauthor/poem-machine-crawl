#!/usr/local/bin/python3

# todos/enhancements:
# - input ranges in "A-B" format, or allow specific number
# - automatically populate text input options, based on contents of texts/
# - include error detection on invalid inputs
#   - check if custom file exists
#   - check if limits are integers
#   - check if upper limits are greater than lower limits
#     - print("You must enter a number greater than {}.".format(words_lower_limit))
#     - print("You must enter a number greater than {}.".format(lines_lower_limit))
# + add end option to repeat, restart, or exit
# + add poem count
# + add error detection to initial text input
# + tidy formatting

from random import randrange, sample

def gather():
    words_lower_limit = 5
    words_upper_limit = 10
    corpus_path = "/Users/grantrosson/Dropbox/Code/poem-machine/texts/dickinson.txt"

   # open corpus from file and read into memory
    with open(corpus_path, 'rt') as corpus:
    
        data = corpus.read()
    
        # make each word an item in an array
        wordlist = data.split()

    lines = []
    for i in range(0,500) : 
        line = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
        lines.append(line)
    poem = '<br>'.join(lines)

    return poem

