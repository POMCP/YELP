'''This file implements  the prediction functionality'''
import numpy as np
from operator import itemgetter, truediv


def rating_predictor(bid, ldamodel, dictionary, df_r, df_b):
    '''Topic classes'''
    # service = [12, 14, 15, 16, 17, 20, 21, 23, 24, 28, 29, 30, 31, 32, 33, 36, 39, 40, 41, 42, 43, 45, 48, 49]
    # food = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 22, 25, 26, 27, 34, 35, 37, 38, 44, 46, 47]
    mexican = [1, 31, 49, 48]
    american = [8, 10, 11, 15, 20, 27, 33, 35, 37, 41, 45, 46]
    service = [0, 7, 9, 13, 16, 22, 24, 25, 28, 30, 39, 42]
    breakfast = [18, 32, 43]
    bar = [2, 17, 23, 34, 36, 38]
    lunch = [3, 4, 12, 40]
    decor = [14, 19]
    value = [5, 29]
    asian = [26, 44, 47]

    data = df_r[df_r['business_id'] == bid]

    '''Topic prediction'''
    sum_stars = list(np.zeros(9))
    count_review = list(np.zeros(9))
    data = data.reset_index()

    for i, item in data.iterrows():
        p = ldamodel.get_document_topics(dictionary.doc2bow(item['text'].lower().split()))
        topic = max(p, key=itemgetter(1))[0]
        if topic in mexican:
            count_review[0] += 1
            sum_stars[0] += item['stars']
        elif topic in american:
            count_review[1] += 1
            sum_stars[1] += item['stars']
        elif topic in service:
            count_review[2] += 1
            sum_stars[2] += item['stars']
        elif topic in breakfast:
            count_review[3] += 1
            sum_stars[3] += item['stars']
        elif topic in bar:
            count_review[4] += 1
            sum_stars[4] += item['stars']
        elif topic in lunch:
            count_review[5] += 1
            sum_stars[5] += item['stars']
        elif topic in decor:
            count_review[6] += 1
            sum_stars[6] += item['stars']
        elif topic in value:
            count_review[7] += 1
            sum_stars[7] += item['stars']
        elif topic in asian:
            count_review[8] += 1
            sum_stars[8] += item['stars']

    # star_prediction = map(lambda x_y: truediv(*x_y), filter(lambda x_y: x_y[1] != 0, zip(sum_stars, count_review)))
        star_prediction = [truediv(x, y) if y else 0 for x, y in zip(sum_stars, count_review)]

    print '==================================================='
    print 'Star prediction for ', list(df_b['name'][df_b['business_id'] == bid])[0]
    print 'Overall Rating ', list(df_b['stars'][df_b['business_id'] == bid])[0]
    print '==================================================='
    print 'Mexican ', [item if item != 0 else 'Not Rated' for item in [star_prediction[0]]][0]
    print 'American ', [item if item != 0 else 'Not Rated' for item in [star_prediction[1]]][0]
    print 'Service ', [item if item != 0 else 'Not Rated' for item in [star_prediction[2]]][0]
    print 'Breakfast ', [item if item != 0 else 'Not Rated' for item in [star_prediction[3]]][0]
    print 'Bar ', [item if item != 0 else 'Not Rated' for item in [star_prediction[4]]][0]
    print 'Lunch ', [item if item != 0 else 'Not Rated' for item in [star_prediction[5]]][0]
    print 'Decor ', [item if item != 0 else 'Not Rated' for item in [star_prediction[6]]][0]
    print 'Value ', [item if item != 0 else 'Not Rated' for item in [star_prediction[7]]][0]
    print 'Asian ', [item if item != 0 else 'Not Rated' for item in [star_prediction[8]]][0]
    return star_prediction
