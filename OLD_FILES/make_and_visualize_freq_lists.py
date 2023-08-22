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
    print ("Different types of tokens are : ", types)
    print ("The TTR (Type by Tokens Ratio) is :", ttr)

    return token_count, unique_words


def frequency_list (token_count, file_name):
    #convert dict to list and sort using frequency
    #token_ranks is a 2d-matrix with each row contaning 1 - token and 2 - it's count
    token_ranks = []
    for i in token_count:
        token_ranks.append([i, token_count[i]])
    
    token_ranks.sort(key = lambda x:x[1], reverse = True)


    with open(file_name, 'w') as file:
        file.writelines("%s\n" % place for place in token_ranks)

    print ("Top 20 tokens and their frequency : \n",token_ranks[:20])


def transform (freq_file, pure_file):

    with open(freq_file, 'r') as f:
            ar = [x.strip() for x in f.readlines()]
            for i in range(len(ar)):
                    ar[i] = int(ar[i].split()[-1][:-1])

    with open(pure_file, 'w') as f:
            for x in ar:
                    print(x, file=f)


def plot_freq_list ():
        with open("avar1_pure.txt", 'r') as f:
                ar1 = [float(x) for x in f.read().strip().split()][:100000]
                # ar1.reverse()

        with open("avar2_pure.txt", 'r') as f:
                ar2 = [float(x) for x in f.read().strip().split()][:100000]
                # ar2.reverse()

        with open("tom_pure.txt", 'r') as f:
                ar3 = [float(x) for x in f.read().strip().split()][:100000]
                # ar3.reverse()

        with open("tkt_pure.txt", 'r') as f:
                ar4 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        with open("chir1_pure.txt", 'r') as f:
                ar5 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        with open("chir2_pure.txt", 'r') as f:
                ar6 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        with open("anna_pure.txt", 'r') as f:
                ar7 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        #print(sum(ar1), sum(ar2), sum(ar3), sum(ar4))

        plt.plot(list(range(len(ar1))), ar1, label="avar 1 (36 155 tokens)")
        plt.plot(list(range(len(ar2))), ar2, label="avar 2 (49 141 tokens)")
        plt.plot(list(range(len(ar3))), ar3, label="tom sawyer (76 664 tokens)")
        plt.plot(list(range(len(ar4))), ar4, label="tokita (13 337 tokens)")
        plt.plot(list(range(len(ar5))), ar5, label="chir 1 (210 274 tokens)")
        plt.plot(list(range(len(ar6))), ar6, label="chir 2 (212 291 tokens)")
        plt.plot(list(range(len(ar7))), ar7, label="anna karenina (269 580 tokens)")

    ##    plt.plot(list(range(len(ar1))), ar1, label="avar 1 (26 363 tokens)")
    ##    plt.plot(list(range(len(ar2))), ar2, label="avar 2 (26 306 tokens)")
    ##    plt.plot(list(range(len(ar3))), ar3, label="tom sawyer (26 371 tokens)")
    ####    plt.plot(list(range(len(ar4))), ar4, label="tokita (13 337 tokens)")
    ##    plt.plot(list(range(len(ar5))), ar5, label="chir 1 (26 370 tokens)")
    ##    plt.plot(list(range(len(ar6))), ar6, label="chir 2 (26 395 tokens)")
    ##    plt.plot(list(range(len(ar7))), ar7, label="anna karenina (26 353 tokens)")
        plt.ylabel('Frequency')
        plt.xlabel('rank')
        plt.legend()
        plt.show()

def plot_heap ():

    unique_words_tom = tokenization ("tom.txt")[1]
    unique_words_avar1 = tokenization ("avar1.txt")[1]
    unique_words_avar2 = tokenization ("avar2.txt")[1]
    unique_words_tkt = tokenization ("tkt.txt")[1]
    unique_words_chir1 = tokenization ("chir1.txt")[1]
    unique_words_chir2 = tokenization ("chir2.txt")[1]
    unique_words_anna = tokenization ("anna.txt")[1]

    m=500
    plt.plot([(i+1)*m for i in range(len(unique_words_tom))], [i for i in unique_words_tom], label="tom sawyer (76 664 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_avar1))], [i for i in unique_words_avar1], label="avar 1 (36 155 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_avar2))], [i for i in unique_words_avar2], label="avar 2 (49 141 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_tkt))], [i for i in unique_words_tkt], label="tokita (13 337 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_chir1))], [i for i in unique_words_chir1], label="chir 1 (210 274 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_chir2))], [i for i in unique_words_chir2], label="chir 2 (212 291 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_anna))], [i for i in unique_words_anna], label="anna karenina (269 580 tokens)")
    plt.ylabel('Different types of tokens')
    plt.xlabel('Total no. of tokens')
    plt.legend()
    plt.show()

def main ():
    #token_count = tokenization ("tom_30.txt")
    token_count = tokenization ("tom.txt")[0]
    frequency_list (token_count, "tom_freq.txt")
    transform ("tom_freq.txt", "tom_pure.txt")

    #token_count = tokenization ("avar1_30.txt")
    token_count = tokenization ("avar1.txt")[0]
    frequency_list (token_count, "avar1_freq.txt")
    transform ("avar1_freq.txt", "avar1_pure.txt")

    #token_count = tokenization ("avar2_30.txt")
    token_count = tokenization ("avar2.txt")[0]
    frequency_list (token_count, "avar2_freq.txt")  
    transform ("avar2_freq.txt", "avar2_pure.txt")

    token_count = tokenization ("tkt.txt")[0]
    frequency_list (token_count, "tkt_freq.txt")  
    transform ("tkt_freq.txt", "tkt_pure.txt")

##    token_count = tokenization ("chir.txt")
##    frequency_list (token_count, "chir_freq.txt")  

    #token_count = tokenization ("chir1_30.txt")
    token_count = tokenization ("chir1.txt")[0]
    frequency_list (token_count, "chir1_freq.txt")  
    transform ("chir1_freq.txt", "chir1_pure.txt")

    #token_count = tokenization ("chir2_30.txt")
    token_count = tokenization ("chir2.txt")[0]
    frequency_list (token_count, "chir2_freq.txt")
    transform ("chir2_freq.txt", "chir2_pure.txt")

    #token_count = tokenization ("anna_30.txt")
    token_count = tokenization ("anna.txt")[0]
    frequency_list (token_count, "anna_freq.txt")
    transform ("anna_freq.txt", "anna_pure.txt")

    #plot_freq_list ()

    plot_heap ()


if __name__ == '__main__':
    main ()
