# USED CAR RECOMMENDATION SYSTEM IN SINGAPORE

### ABOUT
---
this is our SC1015 mini project which focuses on analysing the used car market in Singapore to help buyers decide if a used car is worth it or not.
We focused on data retrieved from Sgcarmart.com which is the largest website for used car listings in Singapore. For detailed walkthrough, please view the source code in order from:

1. [Data Collection](https://github.com/nathanpua/SC1015/tree/main/Data_Collection)
2. [Data Cleaning and Visualisation](https://github.com/nathanpua/SC1015/blob/main/EDA.ipynb)
3. [Regession Analysis](https://github.com/nathanpua/SC1015/blob/main/regression.ipynb)

### PROBLEM DEFINITION
---
* Are we able to predict the price of a car based on its attributes?
* What variables should we use to determine the price of a car?
* is a car worth buying? by comparing predicted and actual price
* Which model should we use to predict the price of a car?

### MODELS USED
---
1. Linear Regression  
2. Random Forest Regression  
3. K-Nearest-Neighbours Regression
4. Neural Network Regression

 And 2 more models that we did not present:  
 5. Polynomial Regression (Degree 2)  
 6. Elastic Net Regression  

### CONCLUSION
---
* Most of our models achieved a good explained variance scores (> 0.90)
* We explored many different regression models
* The worst performing model was the K-Nearest-Neighbours Regression. This is because the model depends greatly on distances between points, and since we had high dimensions due to many predictor variables, the distances were less representative resulting in poorer explained variance and RMSE
* Neural Network regression came in second place, close to our best model which was Random forest regression. We did not fine tune parameters for the Neural network regression so it could possibly have been the best model.
* We decided to use the random forest regression model to build the recommendation system which predicted car prices and compared them to the actual prices to find good deals. [Here is the list of recommmended cars based on our dataset](https://github.com/nathanpua/SC1015/blob/main/datasets/reccomended.csv)

### INSIGHTS GAINED FROM THIS PROJECT
---
* Web scraping with beautifulsoup to scrape data from websites
* Searching in the HTML for the required variables and writing functions to extract these data and dealing with errors as the HTML was not consistent in some of the listings
* Learnt about random forest regression
* Learnt about K-Nearest-Neighbours regression
* Learnt Neural Networks, Keras and Tensorflow
* Utilising the K-Folds cross validation method to achieve more objective regression metrics


### REFERENCES
---
* https://www.sgcarmart.com/used_cars/index.php
* https://stackoverflow.com/questions/46490626/getting-all-links-from-a-page-beautiful-soup
* https://realpython.com/beautiful-soup-web-scraper-python/
* https://medium.com/@nandiniverma78988/neural-network-regression-implementation-and-visualization-in-python-d5893713ed79
* https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
* https://aamir07.medium.com/knn-regression-with-python-c11cbc5aa9a8
* https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html



