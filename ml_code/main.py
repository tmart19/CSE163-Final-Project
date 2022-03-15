from MachineLearning import gender_pay_decision_tree
from MachineLearning import gender_pay_random_forest
from MachineLearning import race_pay_decision_tree
from MachineLearning import race_pay_random_forest
from MachineLearning import degree_level_pay_decision_tree
from MachineLearning import degree_level_pay_random_forest
from MachineLearning import region_pay_decision_tree
from MachineLearning import region_pay_random_forest


INCOME_DATA = './datasets/PanelStudyIncomeDynamics.csv'


def ml_methods(data):
    """
    Contains method calls to ML models that predict salary
    based on various attributes.
    """
    gender_pay_decision_tree(data)
    gender_pay_random_forest(data)
    race_pay_decision_tree(data)
    race_pay_random_forest(data)
    degree_level_pay_decision_tree(data)
    degree_level_pay_random_forest(data)
    region_pay_decision_tree(data)
    region_pay_random_forest(data)


def main():
    ml_methods(INCOME_DATA)


if __name__ == '__main__':
    main()
