import pandas as pd
import numpy as np
import math

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor


def gender_pay_decision_tree(data):
    """
    Predicts annual income amount by gender using DecisionTreeRegressor.
    """
    income_data = pd.read_csv(data)
    features = income_data[['sex']]
    labels = income_data['annlabinc']

    model = DecisionTreeRegressor()
    mean_error = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income using "
          "gender data on DecisionTreeRegressor:", mean_error)


def gender_pay_random_forest(data):
    """
    Predicts annual income amount by gender using RandomForestRegressor.
    """
    income_data = pd.read_csv(data)
    features = income_data[['sex']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income using "
          "gender data - RandomForestRegressor:", standard_deviation)


def race_pay_decision_tree(data):
    """
    Predicts annual income amount by gender using RandomForestRegressor.
    """
    income_data = pd.read_csv(data)
    features = income_data[['white', 'black', 'hisp', 'othrace']]
    labels = income_data['annlabinc']

    model = DecisionTreeRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using racial data - DecisionTreeRegressor:",
          standard_deviation)


def race_pay_random_forest(data):
    income_data = pd.read_csv(data)
    features = income_data[['white', 'black', 'hisp', 'othrace']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using racial data - RandomForestRegressor:",
          standard_deviation)


def degree_level_pay_decision_tree(data):
    income_data = pd.read_csv(data)
    income_data = income_data[['degree', 'annlabinc']]
    income_data = income_data.dropna()

    features = income_data[['degree']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using highest degree received data - DecisionTreeCLassifier:",
          standard_deviation)


def degree_level_pay_random_forest(data):
    income_data = pd.read_csv(data)
    income_data = income_data[['degree', 'annlabinc']]
    income_data = income_data.dropna()

    features = income_data[['degree']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using highest degree received data - RandomForestClassifier:",
          standard_deviation)


def region_pay_decision_tree(data):
    income_data = pd.read_csv(data)
    income_data = income_data[['region', 'annlabinc']]
    income_data = income_data.dropna()

    features = income_data[['region']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using region data - DecisionTreeClassifier:",
          standard_deviation)


def region_pay_random_forest(data):
    income_data = pd.read_csv(data)
    income_data = income_data[['region', 'annlabinc']]
    income_data = income_data.dropna()

    features = income_data[['region']]
    labels = income_data['annlabinc']

    model = RandomForestRegressor()
    standard_deviation = get_cv(model, features, labels)
    print("Mean error of predicted income to actual income "
          "using region data - RandomForestClassifier:",
          standard_deviation)


def get_cv(model, features, labels):
    """
    Takes in a model, features columns, and label columns as parameters and
    calculates cross validation score by fitting model and generating a
    negative mean squared error. Performs 5 fold cross validation and
    returns the mean error among all 5 folds.
    """
    cv_score = cross_val_score(model, features, labels,
                               scoring='neg_mean_squared_error', cv=5)
    cv_score = cv_score * -1
    sqrt_vals = []
    for value in cv_score:
        mean_error = math.sqrt(value)
        sqrt_vals.append(mean_error)
    return np.sum(sqrt_vals) / len(cv_score)
