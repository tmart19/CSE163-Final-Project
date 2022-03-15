import pandas as pd

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
    standard_deviation = cv_score.sum() / len(cv_score)
    return standard_deviation
