#based on this code: https://github.com/ayushgarg31/NLP-Assignment-1

from nltk.tokenize import word_tokenize
import re
from matplotlib import pyplot as plt
from json import dumps

def tokenization (path):
    #open file and convert it to lower case
    file = open(path, "r", encoding="utf8")
    txt = file.read()
    txt_lower = txt.lower()

    #remove all special characters except - and _
    special_chars = re.compile('[`~!@#$%^&*()+={}|\[\]:";<>?,\./“”]')
    txt_lower = special_chars.sub("", txt_lower)

    #tokenize using word_tokenizer
    #token_list is a list of tokens
    tokens_list = word_tokenize(txt_lower)
    tokens_list = [i for i in tokens_list if len(re.findall('[а-яa-z0-9]', i))!=0]
    tokens = len(tokens_list)

    file.close()

    #count the number of times each token appears and save it in dictionary
    #token_count is a dictionary with tokens as keys and their frequency as value
    m = 500
    token_count = {}
    counter = 0
    unique_words = []
    for i in tokens_list:
        if (i in token_count.keys()):
            token_count[i] += 1
        else:
            token_count[i] = 1
    
        #count types after every m tokens for Heap's law
        if (counter%m == 0):
            unique_words.append(len(token_count.keys()))
        counter += 1
        
    unique_words = unique_words[1:]
    types = len(token_count.keys())
    ttr = types/tokens

    print("\nText : ", path)
    print ("The total number of tokens are : ", tokens)
##    print ("Different types of tokens are : ", types)
##    print ("The TTR (Type by Tokens Ratio) is :", ttr)

    return token_count


def frequency_list (token_count, file_name):
    #convert dict to list and sort using frequency
    #token_ranks is a 2d-matrix with each row contaning 1 - token and 2 - it's count
    token_ranks = []
    for i in token_count:
        token_ranks.append([i, token_count[i]])
    
    token_ranks.sort(key = lambda x:x[1], reverse = True)


    with open(file_name, 'w') as file:
        file.writelines("%s\n" % place for place in token_ranks)

    #print ("Top 20 tokens and their frequency : \n",token_ranks[:20])



def main ():
    languages = ['agx-folk', 'ava-folk', 'kum-folk', 'rut-folk', 'dar-folk', 'tab-folk',
                 'lak-folk', 'lez-folk', 'nog-folk', 'tkr-folk', 'tat-folk', 'rus-folk',
                 'arch-folk', 'khv-folk']
    #languages = ['dar']




    for language in languages:
        path = "../folklore_texts/%s.txt" % language
        token_count = tokenization (path)
##        file_name = language + "_freq.txt"
##        frequency_list (token_count, file_name)







if __name__ == '__main__':
    main ()
