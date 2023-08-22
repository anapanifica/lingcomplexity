#based on this code: https://github.com/ayushgarg31/NLP-Assignment-1

import pandas as pd
import re
from json import dumps

def syllabify (word): #this function makes double hyphens at syllable boundaries

    consonants = "b|bʷ|c|č|č̃|c̊|c̃|c\'|č\'|c̊\'|c̃\'|c\'ː|č\'ː|c\'ːʷ|c\'ʲ|c\'ʷ|č\'ʷ|cː|čː|c̊ː|čːʷ|čːˤ|cᶣ|cʷ|čʷ|c̃ʷ|čˤ|č̃ˤ|d|dː|dʲ|dʷ|f|fː|g|gː|gʲ|gʷ|ɢ|ɢʷ|ɢˤ|ɣ|h|ħ|hʷ|hˤ|ʜ|j|k|k̃|k\'|k\'ː|k\'ːʷ|k\'ʲ|k\'ʷ|k\'ʷʲ|k\'ɏ|kː|kːʲ|kːʷ|kʲ|kʲ\'|kʲʷ|kᶣ|kʷ|k̃ʷ|l|lʲ|lʷ|ʟ|ʟ\'|ʟ\'ː|ʟ\'ːʷ|ʟ\'ʷ|ʟː|ʟʷ|ɬ|ɬː|ɬːʷ|ɬʷ|m|n|nʲ|nʷ|nɏ|p|p̃|p\'|pː|q|q̃|q\'|q\'ː|q\'ːʷ|q\'ːˤ|q\'ʷ|q\'ʷˤ|q\'ˤ|qː|qːʲ|qːʷ|qːʷˤ|qːˤ|qʲ|qᶣ|qʷ|q̃ʷ|qʷˤ|qˤ|q̃ˤ|r|Ř|r̭|rʷ|ʁ|ʁʷ|ʁʷˤ|ʁˤ|s|š|s̊|s\'|s\'ʷ|sː|šː|s̊ː|šːʲ|sːʷ|šːʷ|sʲ|sʷ|šʷ|šˤ|t|t̃|t\'|t\'ʲ|t\'ʷ|tː|tːʷ|tʲ|tʷ|t̃ʷ|v|w|x|x̌|xː|xːʲ|xːʷ|xʲ|xʷ|xʷʲ|z|ž|z̊|zʲ|zʷ|žʷ|žˤ|ʒ|ǯ|ʒ̊|ǯʷ|ʔ|ʔʷ|ʔˤ|ʕ|ʕʷ|ʡ|χ|χː|χːʷ|χːʷˤ|χːˤ|χʲ|χʷ|χʷˤ|χˤ"
    vowels = "a|ǎ|ä|ä̃|ã|ḁ|ḁ̈|aː|ǎː|äː|ãː|aːˤ|aˤ|äˤ|ãˤ|e|ě|ẽ|e̥|eː|ẽː|eˤ|ə|ə̃|i|ĩ|i̥|i̭|iː|ĩː|iˤ|ɨ|ɨ̃|ɨː|ɨˤ|o|ö|ö̃|õ|oː|öː|õː|oːˤ|oˤ|ɵ|ɵ̃|u|ü|ũ|u̥|ṷ|ṷ̈|uː|üː|ũː|uˤ|ṷˤ"


    word = re.sub('((?:' + vowels + ')-(?:' + consonants + '))-((?:' + consonants + ')-)', r"\1--\2", word) # V-C-C- > V-C--C-
    word = re.sub('(' + vowels + ')-((?:' + consonants + ')-(?=' + vowels + '))', r"\1--\2", word) # V-C-V > V--C-V
    #print(word)


    return word

def count_phonemes_and_types (words):
    #phoneme_list = re.split(" |-", words) #uncomment this to count the number of unique phonemes
    phoneme_list = re.split(" |--", syllabify(words)) #uncomment this to count the number of unique syllables

    #count the number of times each phoneme appears and save it in dictionary
    #phoneme_count is a dictionary with phonemes as keys and their frequency as value
    m = 1
    phoneme_count = {}
    counter = 0
    types_count = {}
    for i in phoneme_list:
        if (i in phoneme_count.keys()):
            phoneme_count[i] += 1
        else:
            phoneme_count[i] = 1
    
        #count types after every m phonemes for Heap's law
        if (counter%m == 0):
            types_count [counter] = len(phoneme_count.keys())
        counter += 1

    #print(types_count)
##    types = len(phoneme_count.keys())
##    ttr = types/phonemes

    return phoneme_count, types_count


def make_frequency_list (phoneme_count):
    
    #convert dict to list and sort using frequency
    #phoneme_ranks is a 2d-matrix with each row contaning 1 - phoneme and 2 - it's count
    phoneme_ranks = []
    for i in phoneme_count:
        phoneme_ranks.append([i, phoneme_count[i]])
    
    phoneme_ranks.sort(key = lambda x:x[1], reverse = True)

    phoneme_ranks_for_print = "f\ttype\n" #names of columns as required for tfl format

    for word in phoneme_ranks:
        phoneme_ranks_for_print = phoneme_ranks_for_print + str(word [1]) + "\t" + word [0] + "\n"
    print (phoneme_ranks_for_print[0:50])

    return phoneme_ranks_for_print

def make_types_count_file (type_count):
    
    type_count_for_print = "N\tV\n" #names of columns as required for vgc format

    for t in type_count.keys():
        type_count_for_print = type_count_for_print + str(t) + "\t" + str(type_count[t]) + "\n"
    print (type_count_for_print[0:50])

    return type_count_for_print

def main ():
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
        
        long_string = long_string.replace("g", "g")

        #remove stress
        long_string = long_string.replace("á", "a").replace("ã́", "ã").replace("ä́", "ä").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ě́", "ě").replace("ĩ́","ĩ").replace("ǎ́", "ǎ").replace("ǘ", "ü").replace("ɨ́", "ɨ").replace("ḁ́", "ḁ").replace("ḁ̈́", "ḁ̈").replace("ṹ", "ũ")

        #merge allophones
        long_string = long_string.replace("i̭", "i").replace("r̭", "r").replace("ṷ", "u").replace("ṷ̈", "ü").replace("ṷˤ", "uˤ")
        if language == "Khlyut":
            long_string = long_string.replace("ǎ", "a")

        #correct typos
        if language == "Gigatli":
            long_string = long_string.replace("ä", "а")
        if language == "Burshag":
            long_string = long_string.replace("ɵ", "e")
    
        words = long_string.strip("-")

 
        #frequency lists (data for type frequency list (tfl))

        phoneme_count = count_phonemes_and_types (words)[0]
        phoneme_ranks_for_print = make_frequency_list (phoneme_count)

        #path = 'frequency_lists_kiko_phonemes/' + str(language) + "_freq.txt"
        path = 'frequency_lists_kiko_syllables/' + str(language) + "_freq.txt"
        f = open (path, 'w', encoding = 'utf-8')
        f.write (phoneme_ranks_for_print)
        f.close

        # the number of types after each m phonemes (data for vocabulary growth curve (vgc))

        type_count = count_phonemes_and_types (words)[1]
        type_count_for_print = make_types_count_file (type_count)

        #path = 'type_counts_kiko_phonemes/' + str(language) + "_type_counts.txt"
        path = 'type_counts_kiko_syllables/' + str(language) + "_type_counts.txt"
        f = open (path, 'w', encoding = 'utf-8')
        f.write (type_count_for_print)
        f.close 
        


if __name__ == '__main__':
    main ()
