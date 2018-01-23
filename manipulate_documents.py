#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gensim
from exsim import document

if __name__ == '__main__':
    # Make text file from database
    # document.make_text_file_from_database(1, 'where res.pal="kyoto"', '../../data/docs/tabelog/kyoto_prs.txt')
    # document.make_text_file_from_database(1, 'where res.pal="osaka"', '../../data/docs/tabelog/osaka_prs.txt')
    # document.make_text_file_from_database(1, 'where res.pal="hyogo"', '../../data/docs/tabelog/hyogo_prs.txt')

    # document.make_text_file_from_database(2, 'where res.pal="kyoto"', '../../data/docs/tabelog/kyoto_reviews_prs.txt')
    # document.make_text_file_from_database(2, 'where res.pal="osaka"', '../../data/docs/tabelog/osaka_reviews_prs.txt')
    # document.make_text_file_from_database(2, 'where res.pal="hyogo"', '../../data/docs/tabelog/hyogo_reviews_prs.txt')
    # document.diveide_texts('../../data/docs/test/test_reviews.txt', '../../data/docs/test/test_reviews_divided.txt')
    # docs = document.Documents()
    # docs.read_documents('../../data/docs/test/test_divided.txt')

    docs = document.Documents()
    docs.read_documents('../../data/docs/test/test_divided_replaced_5.txt')
    # print(len(docs.documents))
    # print(docs.documents[0])
    # print(docs.documents[0].words)
    docs.read_experience_list('chie-extracted2')
    # print(docs.experiences.experiences[0])
    # print(docs.experiences.experiences[0].modifier)
    docs.make_replace_dict()
    # print(docs.replace_dict)
    # 「飲む」という語に注目．「飲む」の10語以内にある経験をなす語(experiencesに含まれる語)を記号に置き換える．
    # docs.replace_experiences_with_symbols('飲む', 5)
    # docs.write_documents('../../data/docs/test/test_divided_replaced_5.txt')



    docs.get_words_frequencies_around_experiences(15)
    print(docs.words_frequencies_around_experiences)
