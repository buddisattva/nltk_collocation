from nltk import collocations
import os
from os import walk
import csv

os.chdir(os.path.dirname(__file__) + "/世界和平日")

filelist = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    filelist.extend(filenames)
    break

# 把目錄下所有TXT檔案加到list裡面
txtfilelist = []
for filename in filelist:
    if os.path.splitext(filename)[1] == '.txt':
        txtfilelist.append(filename)

# 準備好要紀錄資訊的csv檔
csvfile = open("世界和平日.csv", 'w', encoding='UTF-8')

for current_txtfilename in txtfilelist:

    current_title = current_txtfilename.strip('.txt')
    print(current_title + "：")
    csvfile.write(current_title + '\n')

    file = open(current_txtfilename, "r")
    words = file.read().split(' ')

    # Bigram
    bigram_measures = collocations.BigramAssocMeasures()
    bigram_finder = collocations.BigramCollocationFinder.from_words(words)

    bigram_finder.apply_freq_filter(2)  # 詞組至少出現幾次才跑共現的設定
    for bigram in bigram_finder.score_ngrams(bigram_measures.raw_freq)[:5]:
        print(bigram)
        list_bigram = list(bigram)
        list_bigram.insert(0, '')
        list_bigram.insert(2, '')
        csvfile.write(str(list_bigram) + '\n')

    # Trigram
    trigram_measures = collocations.TrigramAssocMeasures()
    trigram_finder = collocations.TrigramCollocationFinder.from_words(words)

    trigram_finder.apply_freq_filter(2)  # 詞組至少出現幾次才跑共現的設定
    for trigram in trigram_finder.score_ngrams(trigram_measures.raw_freq)[:5]:
        print(trigram)
        list_trigram = list(trigram)
        list_trigram.insert(0, '')
        csvfile.write(str(list_trigram) + '\n')

    print('\n')
    csvfile.write('\n')

csvfile.close()

