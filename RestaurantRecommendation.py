'''This function recommends a Restaurant for a user based on his review history'''
import numpy as np
from operator import itemgetter, truediv


def recommendation(uid, ldamodel, dictionary, common_data):
    mexican = [1, 31, 49, 48]
    american = [8, 10, 11, 15, 20, 27, 33, 35, 37, 41, 45, 46]
    service = [0, 7, 9, 13, 16, 22, 24, 25, 28, 30, 39, 42]
    breakfast = [18, 32, 43]
    bar = [2, 17, 23, 34, 36, 38]
    lunch = [3, 4, 12, 40]
    decor = [14, 19]
    value = [5, 29]
    asian = [26, 44, 47]

    data = common_data[common_data['user_id'] == uid]

    '''Topic prediction'''
    sum_stars = list(np.zeros(9))
    count_review = list(np.zeros(9))
    total_reviews = len(data)
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
        star_prediction = [round(truediv(x, total_reviews), 2) if total_reviews else 0 for x in count_review]

    print '==================================================='
    print 'Preferences for user: ', list(common_data['name'][common_data['user_id'] == uid])[0]
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
