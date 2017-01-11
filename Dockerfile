FROM python:2.7
ADD DataGeneration.py /
ADD ModelGeneration.py /
ADD RatingPrediction.py /
ADD RestaurantRecommendation.py /
ADD Executable.py /
ADD df_rf.pkl /
ADD df_r.pkl /
ADD df_b.pkl /
ADD df_u.pkl /
ADD User_Preference.svg /
ADD Restaurant_Rating_star.svg /
ADD full_model /
ADD full_model.expElogbeta.npy /
ADD full_model.id2word /
ADD full_model.state /
ADD full_dictionary /
RUN pip install numpy
RUN pip install pandas
RUN pip install nltk
RUN pip install stop_words
RUN pip install gensim
RUN pip install pygal
CMD ["python", "./Executable.py"]