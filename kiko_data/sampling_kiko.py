import re
import pandas as pd
import random

def syllabify (word): #this function adds double hyphens after vowels including vowels in the end of the word
    print(word)
    vowels = ["a", "ǎ", "ä", "ä̃", "ã", "ḁ", "ḁ̈", "aː", "ǎː", "äː", "ãː", "aːˤ", "aˤ", "äˤ", "ãˤ",
              "e", "ě", "ẽ", "e̥", "eː", "ẽː", "eˤ", "ə", "ə̃",
              "i", "ĩ", "i̥", "i̭", "iː", "ĩː", "iˤ", "ɨ", "ɨ̃", "ɨː", "ɨˤ",
              "o", "ö", "ö̃", "õ", "oː", "öː", "õː", "oːˤ", "oˤ",
              "u", "ü", "ũ", "u̥", "ṷ", "ṷ̈", "uː", "üː", "ũː", "uˤ", "ṷˤ"]
    word_syl = ""
    #word = word.replace("-", "")
    print(len(word))
    for x in range(len(word)):
        print(x)
        if (word[x] in vowels) and (x+2 != len(word)):
            word_syl += word[x] + "-"
            x += 3
        else:
            word_syl += word[x]
            x += 1
        print(word_syl)

    
##    for letter in word:
##        if letter in vowels:
##            word_syl += letter + "-"
##        else:
##            word_syl += letter
    word_syl = word_syl.strip("--")
    print(word_syl)
    return word_syl


def sample_words_and_get_values (word_list):
    print("the number of words is ", len(word_list))
    values = []
    for k in range (50):
        i = 0
        word_sample = []
        while i < 1000: # i is a maximal number of letters in a sample
            word = random.choice(word_list) #choose a word
            #print(word)
            try:
                n_of_letters = calculate_ratio (word)[0] # count no. of letters in this word
                #print(n_of_letters)
                word_sample.append(word) # add the word to the sample
                i += n_of_letters
            except ZeroDivisionError:
                print ("Can't find any letters in this word:", word, ".")
        word_sample = ' '.join(word_sample) # unite all sentence in one text
        value = calculate_ratio (word_sample)[2] # 0 for letters; 1 for letter_types; 2 for tlr; 3 for the full list of types
        values.append(value)

    return values


def calculate_ratio(text):
    letters_list = re.split(" |-", text) #count the number of unique phonemes
    #letters_list = re.split(" |--", syllabify(text)) #count the number of unique syllables
    #print(letters_list)
    letters = len(letters_list)
    letters_count = {}
    for i in letters_list:
        if (i in letters_count.keys()):
            letters_count[i] += 1
        else:
            letters_count[i] = 1
    letter_types_list = letters_count.keys()
    letter_types = len(letters_count.keys())
    tlr = letter_types/letters
    #print(letters_count.keys())
##    print ("The total number of letters are : ", letters)
##    print ("Different types of letters are : ", letter_types)
##    print ("The TLR (Type by Letters Ratio) is :", tlr)
    
    return letters, letter_types, tlr, letter_types_list

def main():
    df_full = pd.read_csv('/Users/apanova/OneDrive/Documents/ConLab/LingComplexity/linguistic-complexity/kiko_data/kiko_data.csv', sep=',')
    df_full = df_full.loc[df_full["village"] != "Tpig"] #exclude Tpig because there are only 60 words
    df_full = df_full.loc[df_full["village"] != "Kajtag_Tumenler"] #other villages too because the column `Segments` is not filled for them
    df_full = df_full.loc[df_full["village"] != "Duakar"]
    df_full = df_full.loc[df_full["village"] != "Murego"]
    df_full = df_full.loc[df_full["village"] != "Qunqi"]
    df_full = df_full.loc[df_full["village"] != "Tanti"]
    df_full = df_full.loc[df_full["village"] != "Tsudakhar"]
    df_full = df_full.loc[df_full["village"] != "Xuduc"]
    df = df_full.loc[df_full["village"] != "nan"] #this doesn't work
    
    dict_with_values = {}
    languages = pd.Series(df["village"]).unique()
    #print(languages)
    for language in languages:
        print(language)
        words = df[df['village'] == language]["Segments"].dropna()
        long_string = ""
        for word in list(words):
            long_string = long_string + word + " "
        long_string = long_string.replace(" + ", " ")
        long_string = long_string.replace("é", "e").replace("ú", "u").replace("í", "i").replace("í", "i"). replace("ṹ", "ũ").replace("g", "g")
        long_string = long_string.replace("á", "a").replace("ó", "o").replace("ɨ́", "ɨ").replace("ä́", "ä").replace("ě́", "ě")
        long_string = long_string.replace("ã́", "ã").replace("ḁ́", "ḁ").replace("ǎ́", "ǎ").replace("ǘ", "ü").replace("ḁ̈́", "ḁ̈").replace("ĩ́","ĩ")
        long_string = long_string.strip("-")
        word_list = long_string.split(" ")
        #print(word_list)
        #values = list(calculate_ratio (long_string)[3]) #uncomment this line to calculate values for the whole dataset without sampling
        values = sample_words_and_get_values (word_list)
        dict_with_values[language] = values
        #print(values)

    #print(dict_with_values)

    df = pd.DataFrame(data=dict_with_values) # save results of sampling
    #df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_with_values.items() ])) # uncomment this line to save lists of phonemes
    df_csv = df.to_csv(index=False)
    path = '/Users/apanova/OneDrive/Documents/ConLab/LingComplexity/linguistic-complexity/kiko_data/TLR_50_datapoints_per_language.txt'
    f = open (path, 'w', encoding = 'utf-8')
    f.write (df_csv)
    f.close


if __name__ == '__main__':
    main()
