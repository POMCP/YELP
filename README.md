# YELP Insights
YELP Dataset insights

This project works on the YELP academic dataset to predict latent subtopic ratings for businesses, specifically, Restaurants.
The algorithm is based on the work in paper-
Huang, James, Stephanie Rogers, and Eunkwang Joo. "Improving restaurants by extracting subtopics from yelp reviews." iConference 2014 (Social Media Expo) (2014).
Along with has been included further insights towards generating a smart and more efficient recommendation system that recommeds restaurants to users based on their review comments posted on YELP for respective business.

# Run the code as a docker container 
Open a docker console locally and type in the command- 

docker run sanketshinde/yelp-prediction

This will produce several lines of output.

To run the code locally, run the executable.py file.
Running the code locally will also open two files Restaurant_Rating_star.svg and User_Preference.svg in the browser.
These files show a radar chart that shows the distribution of subtopic ratings for restaurants and preference distribution for users
respectively. In case of an event in which the files do not open in browser, kindly open the respective svg files manually in browser, preferably google chrome or mozilla firefox.

Note: Running the docker container will not show the visualization in browser. Refer to the presentation for verifying the results.
In case of local execution of code form a python interpretor, download the model related files from the shared folder on google drive to the same folder from where the code is run.

# ModelGeneration.py
This file trains and generates the LDA model.

# DataGeneration.py
This file loads the necessary data from the json files.

# RatingPrediction.py
This file contains code that computes and prints out the subtopic ratings for Restaurants buy business ID.

# RestaurantRecommendation.py
This file contains the code that computes and prints out the distibution of user preference to sub topics.

# Executable.py
This is the file that should be run to view the generated insights.
