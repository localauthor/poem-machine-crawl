from random import randrange, sample

def gather(source):
    words_lower_limit = 4
    words_upper_limit = 10

    corpus_path = "static/texts/{}.txt".format(source)

   # open corpus from file and read into memory
    with open(corpus_path, 'rt') as corpus:
    
        data = corpus.read()
    
        # make each word an item in an array
        wordlist = data.split()

    lines = []
    for i in range(0,1000) : 
        line = ' '.join(sample(wordlist, k=randrange(int(words_lower_limit),int(words_upper_limit))))
        lines.append(line)
    poem = '<br>'.join(lines)

    return poem

