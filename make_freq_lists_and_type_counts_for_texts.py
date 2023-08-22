#based on this code: https://github.com/ayushgarg31/NLP-Assignment-1

from nltk.tokenize import word_tokenize
import re
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

    return tokens_list

def count_tokens_and_types (tokens_list):

    #count the number of times each token appears and save it in dictionary
    #token_count is a dictionary with tokens as keys and their frequency as value
    m = 1
    token_count = {}
    counter = 0
    types_count = {}
    for i in tokens_list:
        if (i in token_count.keys()):
            token_count[i] += 1
        else:
            token_count[i] = 1
    
        #count types after every m tokens for Heap's law
        if (counter%m == 0):
            types_count [counter] = len(token_count.keys())
        counter += 1

    #print(types_count)
##    types = len(token_count.keys())
##    ttr = types/tokens

    return token_count, types_count


def make_frequency_list (token_count):
    
    #convert dict to list and sort using frequency
    #token_ranks is a 2d-matrix with each row contaning 1 - token and 2 - it's count
    token_ranks = []
    for i in token_count:
        token_ranks.append([i, token_count[i]])
    
    token_ranks.sort(key = lambda x:x[1], reverse = True)

    token_ranks_for_print = "f\ttype\n" #names of columns as required for tfl format

    for word in token_ranks:
        token_ranks_for_print = token_ranks_for_print + str(word [1]) + "\t" + word [0] + "\n"
    print (token_ranks_for_print[0:50])

    return token_ranks_for_print

def make_types_count_file (type_count):
    
    type_count_for_print = "N\tV\n" #names of columns as required for vgc format

    for t in type_count.keys():
        type_count_for_print = type_count_for_print + str(t) + "\t" + str(type_count[t]) + "\n"
    print (type_count_for_print[0:50])

    return type_count_for_print

def main ():
    languages = ['agx-folk', 'ava-folk', 'kum-folk', 'rut-folk', 'dar-folk', 'tab-folk',  # uncomment this to count tokens in folklore texts
                 'lak-folk', 'lez-folk', 'nog-folk', 'tkr-folk', 'tat-folk', 'arch-folk', 'khv-folk']
    



    
 #   languages = ['agx-luke', 'and-luke', 'ava-luke', 'dar-luke', 'eng-luke', 'lak-luke',  # uncomment this to count tokens in bible texts
 #                'lez-luke', 'rus-luke', 'rut-luke', 'tab-luke', 'udi-luke', 'kum-luke']



    

    for language in languages:
        print(language)
        path = "../folklore_texts/%s.txt" % language
        #path = "../bible_texts/%s.txt" % language
        tokens_list = tokenization (path)
 
        #frequency lists (data for type frequency list (tfl))

        token_count = count_tokens_and_types (tokens_list)[0]
        token_ranks_for_print = make_frequency_list (token_count)

        path = 'frequency_lists_texts/' + language + "_freq.txt"
        f = open (path, 'w', encoding = 'utf-8')
        f.write (token_ranks_for_print)
        f.close

        # the number of types after each m tokens (data for vocabulary growth curve (vgc))

        type_count = count_tokens_and_types (tokens_list)[1]
        type_count_for_print = make_types_count_file (type_count)

        path = 'type_counts_texts/' + language + "_type_counts.txt"
        f = open (path, 'w', encoding = 'utf-8')
        f.write (type_count_for_print)
        f.close 
        


if __name__ == '__main__':
    main ()
