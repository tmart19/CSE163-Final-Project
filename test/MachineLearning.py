import pandas as pd
import numpy as np
import math

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor


def gender_pay_decision_tree(data):
    """
    Predicts annual income amount by gender. Performs 5-fold cross
    validation in order
    """
    income_data = pd.read_csv(data)
    features = income_data[['sex']]
    labels = income_data['annlabinc']

    # find the difference between each row and std
    # maybe take absolute value
    # labels_sd = labels - labels.std()
    # print(labels_sd)

    model = DecisionTreeRegressor()
    standard_deviation = get_cv(model, features, labels)
    print('Standard deviation of predicted income to actual income using \
    gender data - DecisionTreeRegressor:', standard_deviation)


def gender_pay_random_forest(data):
    income_data = pd.read_csv(data)
    features = income_data[['sex']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print('Standard deviation of predicted income to actual income using \
          gender data - RandomForestRegressor:', standard_deviation)


def racial_minority_pay_decision_tree(data):
    income_data = pd.read_csv(data)
    features = income_data[['black', 'hisp', 'othrace']]
    labels = income_data['annlabinc']

    model = DecisionTreeRegressor()
    standard_deviation = get_cv(model, features, labels)
    print('Standard deviation of predicted income to actual income \
          using racial minority data - DecisionTreeRegressor:',
          standard_deviation)


def racial_minority_pay_random_forest(data):
    income_data = pd.read_csv(data)
    features = income_data[['black', 'hisp', 'othrace']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print('Standard deviation of predicted income to actual income \
          using racial minority data - RandomForestRegressor:',
          standard_deviation)


def get_cv(model, features, labels):
    cv_score = cross_val_score(model, features, labels,
                               scoring='neg_mean_squared_error', cv=5)
    cv_score = cv_score * -1
    sqrt_vals = []
    for value in cv_score:
        print(value)
        # mean_error = math.sqrt(value)
        # sqrt_vals.append(mean_error)
    return sqrt_vals
