#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chiebukuro import chiebukuro_analyzer as ca
from chiebukuro import chiebukuro_searcher as cs

if __name__ == '__main__':
    searcher = cs.ChiebukuroSearcher('192.168.1.50', 'chiebukuro')
    # questions = searcher.search_questions_by('\"飲める場所知りませんか\"', 100, ['title', 'body'])
    questions = searcher.search_questions_by_category('ここ、探してます', 105000)
    all_texts = ['']
    counter = 0
    index = 0
    for question in questions:
        all_texts[index] += question['_source']['title'] + question['_source']['body'] + '\n'
        counter += 1
        if counter == 10000:
            counter = 0
            index += 1
            all_texts.append('')

    for i in range(len(all_texts)):
        with open('../../data/chiebukuro/find-place-' + str(i) + 'txt', 'w') as fw:
            fw.write(all_texts[i])

    # analyzer = ca.ChiebukuroAnalyzer(all_text)
    # print(all_text)
