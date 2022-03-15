import sys

import geopandas
import numpy as np
import pandas as pd
import requests
import seaborn
import sklearn
import skimage


from MachineLearning import gender_pay_decision_tree
from MachineLearning import gender_pay_random_forest
from MachineLearning import racial_minority_pay_decision_tree
from MachineLearning import racial_minority_pay_random_forest


INCOME_DATA = './datasets/PanelStudyIncomeDynamics.csv'


def ml_methods(data):
    gender_pay_decision_tree(data)
    gender_pay_random_forest(data)
    racial_minority_pay_decision_tree(data)
    racial_minority_pay_random_forest(data)


def main():
    ml_methods(INCOME_DATA)


if __name__ == '__main__':
    main()
