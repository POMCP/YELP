from gensim import corpora, models
import pandas as pd
from RatingPrediction import *
import pygal
from RestaurantRecommendation import *
import webbrowser

'''Load the lda model'''
ldamodel = models.LdaModel.load('full_model')
dictionary = corpora.Dictionary.load('full_dictionary')

df_b = pd.read_pickle('df_b.pkl')
df_r = pd.read_pickle('df_r.pkl')
# df_u = pd.read_pickle('df_u.pkl')

'''Randomly choose a business id form df_b'''
result = pd.merge(df_b, df_r, how='inner', on='business_id')

'''Predictions'''
print '++++++++++++++++++++++++++++++++++++'
print 'Subtopic ratings for Restaurants'
print '++++++++++++++++++++++++++++++++++++'
stars = []
names = []
'''b_id = ['fjaQ3Ixkofh8xGhklUtDnA', '2SwC8wqpZC4B9iFVTgYT9A', 'eaqJQP6bp7rQJQt5KqfvxQ', 'ym9QwkmB5ZKTyj7q5huTDw',
        'jTGQUWGIVvL-aY03C5BEmw', 'Q9BXMPu2HnRDMq9X_2rHrQ', 'NTfUFk8GyOLL1uPbEO-pVg',  'DE_11y6_vCmPBlbeYskh-Q',
        'pPWre8lbVAssER6CN0uWMw', 'S4TWo9X6b3gU6uucj4JN3g']'''
b_id = ['fjaQ3Ixkofh8xGhklUtDnA', 'eaqJQP6bp7rQJQt5KqfvxQ', 'ym9QwkmB5ZKTyj7q5huTDw']
for i in range(len(b_id)):
    # bid = result['business_id'].loc[np.random.choice(range(len(result)), 1)[0]]
    bid = b_id[i]
    stars.append(rating_predictor(bid, ldamodel, dictionary, df_r, df_b))
    names.append(list(df_b['name'][df_b['business_id'] == bid])[0])
# print 'business_ids: ', b_id

'''Visualization'''
radar_chart = pygal.Radar()
radar_chart.title = 'Latent Topic Ratings'
radar_chart.x_labels = ['Mexican', 'American', 'Service', 'Breakfast', 'Bar', 'Lunch', 'Decor', 'Value', 'Asian']
for i in range(len(b_id)):
    radar_chart.add(names[i], stars[i])
radar_chart.render_to_file('Restaurant_Rating_star.svg')

'''Restaurant Recommendation'''
print '\n'
print '++++++++++++++++++++++++++++++++++++'
print 'Preference distribution for Users'
print '++++++++++++++++++++++++++++++++++++'
# common_data = pd.merge(df_r, df_u, how='inner', on='user_id')
# common_data.to_pickle('common_data')
common_data = pd.read_pickle('common_data.pkl')

# Randomly choose a user ID
preference = []
name = []
u_id = ['yfRrC6MhxpIJ4-xMcrmk5Q', 'nEYPahVwXGD2Pjvgkm7QqQ', 'go2dZIDfrEBqfsGKnA4m7g']
for i in range(len(u_id)):
    # uid = common_data['user_id'].loc[np.random.choice(range(len(common_data)), 1)[0]]
    uid = u_id[i]
    name.append(list(common_data['name'][common_data['user_id'] == uid])[0])
    preference.append((recommendation(uid, ldamodel, dictionary, common_data)))

radar_chart = pygal.Radar()
radar_chart.title = 'User Preferences'
radar_chart.x_labels = ['Mexican', 'American', 'Service', 'Breakfast', 'Bar', 'Lunch', 'Decor', 'Value', 'Asian']
for i in range(len(u_id)):
    radar_chart.add(name[i], preference[i])
radar_chart.render_to_file('User_Preference.svg')

'''Opening charts in web browser'''
url = "http://localhost:63342/YELP_Dataset/Restaurant_Rating_star.svg?_ijt=vfak15toq125804nhbef84ku0d"
webbrowser.open(url, new=2)

url = "http://localhost:63342/YELP_Dataset/User_Preference.svg?_ijt=l210ecc321jh192rseq8ifjs9r"
webbrowser.open(url, new=2)