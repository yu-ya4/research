#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from collections import Counter
from chiebukuro import chiebukuro_analyzer as ca
from chiebukuro import chiebukuro_searcher as cs

if __name__ == '__main__':
    # searcher = cs.ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    # # # questions = searcher.search_questions_by('\"飲める場所知りませんか\"', 100, ['title', 'body'])
    # # questions = searcher.search_questions_by_category('ここ、探してます', 105000)
    # questions = searcher.search_questions_by_category('観光地、行楽地', 670000)
    #
    # # questions = searcher.search_questions_by_category('ここ、探してます', 1000)
    # all_texts = ['']
    # counter = 0
    # index = 0
    # for question in questions:
    #     all_texts[index] += question['_source']['title'] + question['_source']['body'] + '\n'
    #     counter += 1
    #     if counter == 10000:
    #         counter = 0
    #         index += 1
    #         all_texts.append('')
    #
    # for i in range(len(all_texts)):
    #     with open('../../data/chiebukuro/tourist-spots-' + str(i) + '.txt', 'w') as fw:
    #         fw.write(all_texts[i])
    # exit()

    all_modifier_frequencies_counter = Counter({})
    question_files = glob.glob('../../data/chiebukuro/*.txt')
    for question_file in question_files:
        with open(question_file, 'r') as f:
            text = f.read().replace('\n', '')
            analyzer = ca.ChiebukuroAnalyzer(text)
            modifiers_frequences = analyzer.get_modifiers_frequences('食', '../../data/patterns/eat')
            # print(modifiers_frequences)
            modifiers_frequences_counter = Counter(modifiers_frequences)
            all_modifier_frequencies_counter = all_modifier_frequencies_counter + modifiers_frequences_counter

    all_modifiers_frequencies = dict(all_modifier_frequencies_counter)

    with open('../../data/experiences/eat/eat.txt', 'w') as fw1:
        with open('../../data/experiences/eat/eat-freq.txt', 'w') as fw2:

            for key, val in sorted(all_modifiers_frequencies.items(), key=lambda x:x[1], reverse=True):
                fw1.write(key + '\n')
                fw2.write(key + ' ' + str(val) + '\n')
