#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gensim
from exsim import document

if __name__ == '__main__':
    # document.make_text_file_from_database(0, 'where res.pal="kyoto" limit 500', '../../data/docs/test/test_500_reviews.txt')
    # document.diveide_texts('../../data/docs/test/test_500_reviews.txt', '../../data/docs/test/test_500_reviews_divided.txt')
    # exit()
    # Make text file from database
    # document.make_text_file_from_database(1, 'where res.pal="kyoto"', '../../data/docs/tabelog/kyoto_prs.txt')
    # document.make_text_file_from_database(1, 'where res.pal="osaka"', '../../data/docs/tabelog/osaka_prs.txt')
    # document.make_text_file_from_database(1, 'where res.pal="hyogo"', '../../data/docs/tabelog/hyogo_prs.txt')

    # document.make_text_file_from_database(2, 'where res.pal="kyoto"', '../../data/docs/tabelog/kyoto_reviews_prs.txt')
    # document.make_text_file_from_database(2, 'where res.pal="osaka"', '../../data/docs/tabelog/osaka_reviews_prs.txt')
    # document.make_text_file_from_database(2, 'where res.pal="hyogo"', '../../data/docs/tabelog/hyogo_reviews_prs.txt')
    # document.diveide_texts('../../data/docs/test/test_reviews.txt', '../../data/docs/test/test_reviews_divided.txt')
    # docs = document.Documents()
    # docs.read_documents('../../data/docs/test/test_kyoto_reviews_divided.txt')
    #


    # docs = document.Documents()
    # # docs.read_documents('../../data/docs/test/test_500_reviews_divided.txt')
    # docs.read_documents('../../data/docs/test/test_500_reviews_divided.txt', '../../data/docs/test/test_500_reviews.txt.restaurant_ids.txt')
    # docs.read_experience_list('chie-extracted2')
    # docs.make_replace_dict()
    # # #
    # docs.replace_experiences_with_symbols('飲む', 5)
    # docs.write_documents('../../data/docs/test/test_500_reviews_divided_replaced_5.txt')
    # exit()

    docs = document.Documents()
    docs.read_experience_list('chie-extracted2')
    docs.make_replace_dict()
    # docs.read_documents('../../data/docs/test/test_kyoto_reviews_divided_replaced_10.txt')
    docs.read_documents('../../data/docs/test/test_kyoto_reviews_divided_replaced_5.txt')

    exp_docs = docs.make_documents_for_each_experience()
    exp_docs.calc_words_weight()
    i = 0
    for word, weight in sorted(exp_docs.all_documents_weight[32].items(), key = lambda x: x[1], reverse=True):
        if i == 50:
            break
        print(word + ': ' + str(weight))
        i += 1
