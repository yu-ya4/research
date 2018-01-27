#!/usr/bin/env python
# -*- coding: utf-8 -*-

from egmat import tabelog_searcher as ts

cat_list = [('BC', 'BC01', ''), ('BC', 'BC02', ''), ('BC', 'BC03', ''), ('BC', 'BC04', ''), ('BC', 'BC05', ''), ('BC', 'BC06', ''), ('BC', 'BC07', ''), ('BC', 'BC99', ''),
      ('RC', 'RC21', 'RC2101'), ('RC', 'RC21', 'RC2102'), ('RC', 'RC21', 'RC2199')]
cat_list = [('MC', 'MC01', ''), ('MC', 'MC11', ''), ('MC', 'MC21', ''),
             ('CC', 'CC01', ''), ('CC', 'CC02', ''), ('CC', 'CC03', ''), ('CC', 'CC04', ''), ('CC', 'CC05', ''), ('CC', 'CC06', ''), ('CC', 'CC99', ''),
            ('SC', 'SC01', 'SC0101'), ('SC', 'SC01', 'SC0102'), ('SC', 'SC01', 'SC0103'), ('SC', 'SC01', 'SC0199'),
            ('SC', 'SC02', 'SC0201'), ('SC', 'SC02', 'SC0202'), ('SC', 'SC02', 'SC0203'), ('SC', 'SC02', 'SC0299'),
            ('YC', 'YC01', ''), ('YC', 'YC02', ''), ('YC', 'YC99', ''),
            ('RC', 'RC01', 'RC0101'), ('RC', 'RC01', 'RC0102'), ('RC', 'RC01', 'RC0103'), ('RC', 'RC01', 'RC0104'), ('RC', 'RC01', 'RC0105'), ('RC', 'RC01', 'RC0106'), ('RC', 'RC01', 'RC0107'), ('RC', 'RC01', 'RC0108'), ('RC', 'RC01', 'RC0109'), ('RC', 'RC01', 'RC0110'), ('RC', 'RC01', 'RC0111'), ('RC', 'RC01', 'RC0112'), ('RC', 'RC01', 'RC0199'),
            ('RC', 'RC02', 'RC0201'), ('RC', 'RC02', 'RC0202'), ('RC', 'RC02', 'RC0203'), ('RC', 'RC02', 'RC0204'), ('RC', 'RC02', 'RC0209'), ('RC', 'RC02', 'RC0211'), ('RC', 'RC02', 'RC0212'), ('RC', 'RC02', 'RC0213'), ('RC', 'RC02', 'RC0219'),
            ('RC', 'RC03', 'RC0301'), ('RC', 'RC03', 'RC0302'), ('RC', 'RC03', 'RC0303'), ('RC', 'RC03', 'RC0304'),
            ('RC', 'RC04', 'RC0401'), ('RC', 'RC04', 'RC0402'), ('RC', 'RC04', 'RC0403'), ('RC', 'RC04', 'RC0404'), ('RC', 'RC04', 'RC0411'), ('RC', 'RC04', 'RC0412'), ('RC', 'RC04', 'RC0499'),
            ('RC', 'RC12', 'RC1201'), ('RC', 'RC12', 'RC1202'), ('RC', 'RC12', 'RC1203'), ('RC', 'RC12', 'RC1204'), ('RC', 'RC12', 'RC1205'), ('RC', 'RC12', 'RC1299'),
            ('RC', 'RC13', 'RC1301'), ('RC', 'RC13', 'RC1302'),
            ('RC', 'RC14', 'RC1401'), ('RC', 'RC14', 'RC1402'), ('RC', 'RC14', 'RC1403'), ('RC', 'RC14', 'RC1404'), ('RC', 'RC14', 'RC1405'), ('RC', 'RC14', 'RC1406'), ('RC', 'RC14', 'RC1407'), ('RC', 'RC14', 'RC1408'), ('RC', 'RC14', 'RC1409'),
            ('RC', 'RC22', 'RC2201'), ('RC', 'RC22', 'RC2202'), ('RC', 'RC22', 'RC2203'),
            ('RC', 'RC23', ''), ('RC', 'RC99', 'RC9901'), ('RC', 'RC99', 'RC9904'), ('RC', 'RC99', 'RC9903'), ('RC', 'RC99', 'RC9999')
            ]

def get_restaurants_url_not_in_database(conditions, num=0, offset=0):
    searcher = ts.TabelogSearcher()
    saved_restaurants_urls = searcher.get_restaurant_urls_from_db(conditions, num, offset)
    return saved_restaurants_urls

if __name__ == '__main__':
    # tls = ts.TabelogSearcher()
    # review_htmls = tls.get_reviews_from_restaurant('https://tabelog.com/osaka/A2701/A270101/27052831/')
    # print(review_htmls[1])
    # print(len(review_htmls[1]))


    searcher = ts.TabelogSearcher()
    # area_list = searcher.get_area_list_from_db()
    # flg = False
    # for area in area_list:
    #     if (area[0] == 'hyogo'):
    #         print(area)
    #         # if area == ('osaka', 'A2706', 'A270604'):
    #         #     flg = True
    #         # if not flg:
    #         #     continue
    #         for cat in cat_list:
    #             restaurant_htmls, restaurant_urls = searcher.search_for_restaurants('', area[0], area[1], area[2], cat[0], cat[1], cat[2], '', saved_restaurants_urls)
    #             restaurants = searcher.parse_restaurants(restaurant_htmls, restaurant_urls)
    #             searcher.save_restaurants(restaurants)
    #             print(cat)
    # exit()






    # restaurant_url = 'https://tabelog.com/kyoto/A2601/A260201/26003620/'
    # review_htmls, review_urls = searcher.get_reviews_from_tabelog_by_restaurant_url(restaurant_url)
    # reviews = searcher.parse_reviews(review_htmls, review_urls)


    restaurant_urls = searcher.get_restaurant_urls_without_reviews_from_db()
    for restaurant_url in restaurant_urls:
        review_htmls, review_urls = searcher.get_reviews_from_tabelog_by_restaurant_url(restaurant_url)
        reviews = searcher.parse_reviews(review_htmls, review_urls)
        searcher.save_reviews(reviews)
