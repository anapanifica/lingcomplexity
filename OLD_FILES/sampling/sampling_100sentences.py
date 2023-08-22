from nltk.tokenize import word_tokenize
import re
from matplotlib import pyplot as plt
import seaborn as sns
import random

def make_list_with_sentences (path):
    #open file and convert it to lower case
    file = open(path, "r", encoding="utf8")
    txt = file.read()
    txt_lower = txt.lower()
    file.close()

    
    #remove all special characters except - _ . 
    special_chars = re.compile('[`~@#$%^&*()+={}|\[\]:";<>,\/“”]!?')
    txt_lower = special_chars.sub("", txt_lower)


    sentences = txt_lower.split('.')
    sentences = [x for x in sentences if x != '']
    #print(sentences[1:20])

    return sentences


def count_number_of_tokens_and_word_types (sent_sample):
    #tokenize using word_tokenizer
    #token_list is a list of tokens
    sent_sample = ' '.join(sent_sample)
    tokens_list = word_tokenize(sent_sample)
    tokens_list = [i for i in tokens_list if len(re.findall('[а-яa-z0-9]', i))!=0]
    tokens = len(tokens_list)

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
    
    types = len(token_count.keys())
    ttr = types/tokens

##    print ("The total number of tokens are : ", tokens)
##    print ("Different types of tokens are : ", types)
##    print ("The TTR (Type by Tokens Ratio) is :", ttr)

    return tokens, types, ttr

def do_sampling_and_get_values (sentences):
    values = []
    for i in range (1000):
        sent_sample = random.sample(sentences, 100)
        value = count_number_of_tokens_and_word_types (sent_sample)[2] # 0 for tokens; 1 for types; 2 for ttr
        values.append(value)

    return values


def main ():

##    #plotting histograms

##    #histogram with facetization

##    for i, language in enumerate(['agx', 'ava', 'dar', 'eng', 'rus', 'tab']):
##        ax = plt.subplot(3, 2, i + 1)
##        sentences = make_list_with_sentences ("bible_texts/%s-luke.txt" % language)
##        values = do_sampling_and_get_values (sentences)
##        ax.hist(values, bins = 50,
##             color = 'skyblue', edgecolor = 'black')
##        ax.set_title('%s' % language)
##        ax.set_xlabel('number of token types in 100 sentences')
##
##    plt.tight_layout()
##    plt.show()


    #histogram with all languages on the same graph

    languages = ['agx', 'ava', 'dar', 'eng', 'rus', 'tab']
    for language in languages:        
        sentences = make_list_with_sentences ("../bible_texts/%s-luke.txt" % language)
        values = do_sampling_and_get_values (sentences)

        sns.distplot(values, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = language)

    plt.legend(title = 'Language')
    plt.xlabel('TTR in 100 sentences')
    plt.show()


if __name__ == '__main__':
    main ()
