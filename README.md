# CSE163-Final-Project Instructions and Documentation

The code in this ReadMe file corresopnds to the final project for CSE163, Winter Quarter 2022 at the University of Washington. 
Authors: Trinity Martinez and Theo Covich.

Instructions to how to run the code in our project are as follows. The repository for our code contains several folders organized by the data used for our project, as well as our code folders which correspond with our 2 challenge goals: machine learning and learning a new library (Altair). 

1. **viz_code-a directory that houses the code for altair data visualizations that were made for this project.**

    --_DataVis.py_ is a python module that has the code to produce the data visualizations that we made for this project. It uses the main method pattern to run the code blocks that relate to each of our research/investigation questions. This module takes in our data: PSID (Panel Study Income Dynamics) dataset and the Gender Pay dataset as CSVs and uses them to produce the plots.
        1. Is there a gender pay gap?
        2. How does the gender pay gap differ across degree levels achieved for each gender?
        3. Which occupations result in the largest pay gap between men and women? 
        4. How do attributes other than gender (such as race, ethnicity, socio-economic status) contribute to the pay gap? If so, what combination of attributes result in the largest disparity?
    --to run the code in this file follow the steps:
        1. Run the first import lines to load in libraries altair and pandas. 
        2. Clicking on 'run' will run the main method pattern and make corresponding calls to the functions written to produce each plot. 
        3. The plots will generate in a separate html window of your default browser. 
        4. Ensure that the repository has been cloned on your local device in to gain access to the data and the needed information for the project. 

    --_DataVizPlayground.ipynb_ is a Jupyter notebook that was used to test the code and produce plots quickly, before tranferring it to run our actual Python module. The code in this Jupyter Notebook was for experemental and testing purposes only.

2. **ml_code-a directory that contains the code to produce machine learning algorithms that were performed for our project.**

    _MachineLearning.py_ is a Python module that has the code to produce our machine learning model. 

3. **datasets-a directory that contains the datasets that were used in our poejct and analysis.**

    _PanelStudyIncomeDynamics.csv_ 
    _GenderPay.csv_

4. **viz_png-a directory that has PNG images of the plots that are produced for each research question.**

    _#1-gender pay gap_ is a directory conatining PNG images relating to the gender pay gap background information
    _#2-pay across degree_ is a directory containing PNG images relating to the research question of pay across degree earned
    _#3-occupation_ is a directory containing PNG images relating to the research question of pay accross occupation
    _#4-demographics_ is a directory containing PNG images relating to the research question of which combination of attributes result in the worse pay gap between makes and females. 

5. **misc-a directory that has miscallaneous information relating to our proejct. This includes test files, notes from project meetings, and other ifles needed to setup our data science coding environment.**