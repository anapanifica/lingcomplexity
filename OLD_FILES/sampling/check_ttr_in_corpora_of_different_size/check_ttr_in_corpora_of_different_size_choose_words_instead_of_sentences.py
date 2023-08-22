from nltk.tokenize import word_tokenize
import re
from matplotlib import pyplot as plt
import seaborn as sns
import random
import pandas as pd

def make_list_with_words (path):
    #open file and convert it to lower case
    file = open(path, "r", encoding="utf8")
    txt = file.read()
    txt_lower = txt.lower()
    file.close()


    words = word_tokenize(txt_lower)
    words = [i for i in words if len(re.findall('[а-яa-z]', i))!=0] #take only those elements that contain letters


    return words


def count_number_of_tokens_and_word_types (word_sample):

    tokens = len(word_sample)


    #count the number of times each token appears and save it in dictionary
    #token_count is a dictionary with tokens as keys and their frequency as value
##    m = 500
    token_count = {}
##    counter = 0
##    unique_words = []
    for i in word_sample:
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

def do_sampling_and_get_values (words):
    values = []
    for k in range (100):
        i = 0
        word_sample = []

        #these variables are needed for sampling without replacements
        word_numbers = random.sample(range(len(words)), len(words)) #make a shuffled list of numbers of sentences
        word_n = 0 # number of the element in the shuffled list of numbers of sentences


        while i < 1000: # i is a maximal number of tokens in a sample
            #sent = sentences[sent_numbers[sent_n]] #choose a sentence (for sampling without replacements)
            word = random.choice(words) #choose a word (for sampling with replacements)
            #print(sent)
            word_sample.append(word) # add the word to the sample
            i += 1
            word_n += 1
        #print(word_sample)
        value = count_number_of_tokens_and_word_types (word_sample)[2] # 0 for tokens; 1 for types; 2 for ttr
        values.append(value)

    return values


def main ():


    #violinplots with all languages on the same graph


    #languages = ['rus-folk-288889-tokens', 'rus-folk-126928-tokens',
    #             'rus-folk-37070-tokens', 'rus-folk-18852-tokens',
    #             'rus-folk-9437-tokens', 'rus-folk-4992-tokens']

    #languages = ['rus-folk-4992-tokens']

    languages = ['lez-folk-39150-tokens', 'lez-folk-21765-tokens',
                 'lez-folk-11211-tokens', 'lez-folk-5394-tokens']
    #
    
    dict1 = {}
    for language in languages:
        print(language)
        words = make_list_with_words ("/Users/apanova/Library/CloudStorage/OneDrive-Личная/Documents/ConLab/LingComplexity/linguistic-complexity/folklore_texts/%s.txt" % language)
        #count_number_of_tokens_and_word_types (words) #uncomment this line to see the numbers for the whole language without sampling
        values = do_sampling_and_get_values (words)
        dict1[language] = values



    df = pd.DataFrame(data=dict1)


##    df_csv = df.to_csv(index=False)
##    path = '../statistics/TTR_1000_datapoints_per_language_rus.txt'
##    f = open (path, 'w', encoding = 'utf-8')
##    f.write (df_csv)
##    f.close


    index_sort = df.mean().sort_values().index
    df_sorted = df[index_sort]
    # plotting the boxplot for the data  
    sns.violinplot(data = df_sorted) 
  
    # Label x-axis 
    plt.xlabel('Corpora') 
  
    # labels y-axis 
    plt.ylabel('TTR in 100 samples (each sample = 10000 tokens, with replacements)')

    plt.show()



if __name__ == '__main__':
    main ()
