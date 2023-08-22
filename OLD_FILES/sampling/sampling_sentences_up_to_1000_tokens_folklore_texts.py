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
##    special_chars = re.compile('[`~@#$%^&*\(\)+={}|\[\]:";<>,\/\“\”]!\«\»')
##    txt_lower = special_chars.sub("", txt_lower)
##    txt_lower = re.sub("[^а-яa-z0-9.? ]+", '', txt_lower)
##    txt_lower = re.sub(r" +", ' ', txt_lower)


    sentences = re.split('\.', txt_lower)
    sentences = [x for x in sentences if x != ''] # remove empty sentences
    # also manually removed ". . ." fragment in the avar bible
    #print(sentences[1:30])

    return sentences


def count_number_of_tokens_and_word_types (text):
    #tokenize using word_tokenizer
    #token_list is a list of tokens

    tokens_list = word_tokenize(text)
    tokens_list = [i for i in tokens_list if len(re.findall('[а-яa-z0-9]', i))!=0]
    tokens = len(tokens_list)

    #count the number of times each token appears and save it in dictionary
    #token_count is a dictionary with tokens as keys and their frequency as value
##    m = 500
    token_count = {}
##    counter = 0
##    unique_words = []
    for i in tokens_list:
        if (i in token_count.keys()):
            token_count[i] += 1
        else:
            token_count[i] = 1

##        #count types after every m tokens for Heap's law
##        if (counter%m == 0):
##            unique_words.append(len(token_count.keys()))
##        counter += 1
##    if tokens == 0:
##        print ("Can't find any tokens in this sentence:", text)
    types = len(token_count.keys())
    ttr = types/tokens

##    print ("The total number of tokens are : ", tokens)
##    print ("Different types of tokens are : ", types)
##    print ("The TTR (Type by Tokens Ratio) is :", ttr)

    return tokens, types, ttr

def do_sampling_and_get_values (sentences):
    values = []
    for k in range (1000):
        i = 0
        sent_sample = []
        while i < 1000: 
            sent = random.choice(sentences) #choose a sentence
            #print(sent)
            try:
                n_of_tokens = count_number_of_tokens_and_word_types (sent)[0] # count no. of tokens in this sentence
                #print(n_of_tokens)
                sent_sample.append(sent) # add the sentence to the sample
                i += n_of_tokens
            except ZeroDivisionError:
                print ("Can't find any tokens in this sentence:", sent)
        sent_sample = ' '.join(sent_sample) # unite all sentence in one text
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

    languages = ['agx-folklore', 'ava-folklore', 'kum-folklore', 'rut-folklore', 'dar-folklore', 'tab-folklore',
                 'lak-folklore', 'lez-folklore', 'nog-folklore', 'tkr-folklore', 'tat-folklore']
    #languages = ['dar']
    for language in languages:
        print(language)
        sentences = make_list_with_sentences ("../folklore_texts/%s.txt" % language)
        values = do_sampling_and_get_values (sentences)

        sns.distplot(values, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = language)

##    languages = ['rus-anna-karenina', 'eng-tom-sawyer', 'avar-poetry', 'avar-drama']
##    for language in languages:
##        print(language)
##        sentences = make_list_with_sentences ("random_texts_cleaned/%s.txt" % language)
##        values = do_sampling_and_get_values (sentences)
##
##        sns.distplot(values, hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 2}, label = language)

    plt.legend(title = 'Language')
    plt.xlabel('TTR in a sample of random sentences (~ 1000 tokens)')
    plt.show()


if __name__ == '__main__':
    main ()
