#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from exsim import document
from collections import Counter
from chiebukuro import chiebukuro_analyzer as ca

if __name__ == '__main__':


    # for i in range(len(all_texts)):
    #     with open('../../data/chiebukuro/tourist-spots-' + str(i) + '.txt', 'w') as fw:
    #         fw.write(all_texts[i])
    # exit()

    all_modifier_frequencies_counter = Counter({})
    review_files = glob.glob('../../data/docs/tabelog/reviews/drink/all/drink_*_reviews.txt')
    for review_file in review_files:
        # データが大きすぎてメモリにのらなさそうなので分ける
        with open(review_file, 'r') as f:
            text = ''
            i = 0
            for line in f:
                line = line.replace('\n', '')
                text += line
                i += 1
                if i % 10000 == 0:
                    analyzer = ca.ChiebukuroAnalyzer(text)
                    modifiers_frequences = analyzer.get_modifiers_frequences('飲', '../../data/patterns/drink')
                    modifiers_frequences_counter = Counter(modifiers_frequences)
                    all_modifier_frequencies_counter = all_modifier_frequencies_counter + modifiers_frequences_counter
                    text = ''
    all_modifiers_frequencies = dict(all_modifier_frequencies_counter)

    with open('../../data/experiences/drink/around-words/around-drink.txt', 'w') as fw1:
        with open('../../data/experiences/drink/around-words/around-drink-freq.txt', 'w') as fw2:

            for key, val in sorted(all_modifiers_frequencies.items(), key=lambda x:x[1], reverse=True):
                fw1.write(key + '\n')
                fw2.write(key + ' ' + str(val) + '\n')
