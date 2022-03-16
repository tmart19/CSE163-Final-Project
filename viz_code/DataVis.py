import pandas as pd
import altair as alt
alt.renderers.enable('mimetype')

# Research Question #1: Is there a gender pay gap?


def gender_base_pay_bar(gp):
    """
    Produces a bar chart comparing base pay and gender.
    """
    alt.renderers.enable('mimetype')
    gender_base_pay = alt.Chart(gp,
                                title="Base Pay Per"
                                "Gender").mark_bar(color='steelblue'
        ).encode(
            x=alt.X('Gender',
                    axis=alt.Axis(title='Gender (Male or Female)')),
            y=alt.Y('BasePay',
                    axis=alt.Axis(title='Base Pay (in USD)'))
        ).properties(
            width=400, height=600
        )
    gender_base_pay = gender_base_pay.configure_title(fontSize=28)
    gender_base_pay


def gender_annual_income_pie(df):
    """
    Produces a pie chart of female vs male wages.
    """
    gender_annual_income = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field="annlabinc", type="quantitative"),
        color=alt.Color(field="sex", type="nominal",
                        legend=alt.Legend(title="Sex (Male=1, Female=2)")),
    ).properties(
        width=300, height=300,
        title="Annual Income per Gender"
    )
    gender_annual_income.configure_title(fontSize=28)


def gender_bonus_pay_bar(gp):
    """
    Produces a bar chart comparing bonus pay and gender.
    """
    gender_bonus_amount = alt.Chart(gp).mark_bar(
        color='steelblue'
    ).encode(
        x=alt.X('Gender', axis=alt.Axis(title='Gender (Male or Female)')),
        y=alt.Y('Bonus', axis=alt.Axis(title='Bonus Amount (in USD)'))
    ).properties(
        width=400, height=600,
        title="Bonus Amount per Gender"
    )
    gender_bonus_amount = gender_bonus_amount.configure_title(fontSize=28)
    # gender_bonus_amount.save('BonusPayGender.png')


# Research Question #2: How does the gender pay gap differ across degree
# levels achieved for each gender?
def ann_income_degree_bar(df):
    """
    Produces a bar chart comparing annual income and degree obtained,
     grouped by gender.
    """
    gender_ann_income_degree = alt.Chart(
        df, title="Annual Income by Sex and Degree Obtained"
        ).mark_bar().encode(
        x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
        y=alt.Y('annlabinc:Q',
                axis=alt.Axis(
                title='Annual Income in USD')),
        color=alt.Color('sex:N',
                        legend=alt.Legend(title="Sex by Color"
                                                "(1=Male, 2=Female)"),
                        scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('degree:O',
                        title="Degree Levels"
                        "(0=No College Degree,"
                        "1=Bachelor's, 2=Advanced)"),
    ).properties(
        width=200,
        height=700
    )
    gender_ann_income_degree.configure_title(fontSize=28)


def base_pay_education_level(gp):
    """
    Produces a bar chart comparing base pay and education level attained,
    grouped by gender.
    """
    gender_base_pay_education = alt.Chart(gp,
            title="Base Pay by Degree and Sex").mark_bar().encode(
            x=alt.X('Education', axis=alt.Axis(title='Degree')),
            y=alt.Y('BasePay:Q', axis=alt.Axis(title='Annual Income in USD')),
            color=alt.Color('Gender', legend=alt.Legend(title="Sex by Color")),
            column=alt.Column('Gender', title="Gender"),
        ).properties(
        width=200,
        height=700
        )
    gender_base_pay_education.configure_title(fontSize=28)


# Research Question #3: Which occupations result in the
# largest pay gap between men and women?
def job_cat_gender_bar(gp):
    """
    Produces a bar chart comparing base pay for
    each job category, grouped by sex.
    """
    gender_job_cat_base_pay = alt.Chart(gp,
                            title="Base Pay by Job Category and Sex").mark_bar().encode(
        x=alt.X('JobTitle', axis=alt.Axis(title='Job Title')),
        y=alt.Y('BasePay:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('Gender:N', legend=alt.Legend(title="Sex by Color"),
                scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('Gender', title="Gender"),
    ).properties(
        width=200,
        height=700
    )
    gender_job_cat_base_pay.configure_title(fontSize=28)


def job_dept_gender_bar(gp):
    """
    Produces a bar chart comparing base pay for each job department, grouped by sex.
    """
    gender_dept_base_pay = alt.Chart(gp,
        title="Base Pay by Job Department and Sex").mark_bar().encode(
        x=alt.X('Dept', axis=alt.Axis(title='Department')),
        y=alt.Y('BasePay:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('Gender', legend=alt.Legend(title="Sex by Color"), scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('Gender', title="Gender"),
    ).properties(
        width=200,
        height=700
    )
    gender_dept_base_pay = gender_dept_base_pay.configure_title(fontSize=28)
    

# Research Question #4: How do attributes other than gender
# (such as race, ethnicity, socio-economic status) contribute to the pay gap?
# If so, what combination of attributes result in the largest disparity?
def ann_income_hisp(df):
    """
    Produces a bar chart comparing annual income for individuals 
    identifying as Hispanic, grouped by sex.
    """
    gender_hisp_ann_income = alt.Chart(df, 
        title="Annual Income Hispanic and Sex").mark_bar().encode(
        x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
        y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"),
        scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('hisp:O', title="Hispanic (0=No, 1=Yes)"),
    ).properties(
        width=200,
        height=700
    )
    gender_hisp_ann_income = gender_hisp_ann_income.configure_title(fontSize=28)


def ann_income_black(df):
    """
    Produces a bar chart comparing annual income for
    individuals identifying as Black, grouped by sex.
    """
    gender_black_ann_income = alt.Chart(df,
        title="Annual Income Black and Sex").mark_bar().encode(
        x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
        y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"),
        scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('black:O', title="Black (0=No, 1=Yes)"),
    ).properties(
        width=200,
        height=700
    )
    gender_black_ann_income = gender_black_ann_income.configure_title(fontSize=28)


def ann_income_white(df):
    """
    Produces a bar chart comparing annual income for
    individuals identifying as white grouped by sex.
    """
    gender_white_ann_income = alt.Chart(df,
    title="Annual Income White and Sex").mark_bar().encode(
        x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
        y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"),
        scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('white:O', title="White (0=No, 1=Yes)"),
    ).properties(
        width=200,
        height=700
    )
    gender_white_ann_income = gender_white_ann_income.configure_title(fontSize=28)


def ann_income_age(df):
    """
    Produces a plot representing age
    """
    gender_age_ann_income = alt.Chart(df,
        title="Annual Income Age and Sex").mark_bar().encode(
        x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
        y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
        color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"),
        scale=alt.Scale(scheme='darkmulti')),
        column=alt.Column('age', title="age"),
    ).properties(
        width=100,
        height=300
    )
    gender_age_ann_income = gender_age_ann_income.configure_title(fontSize=28)


def ann_income_yrs_exp(df):
    gender_yrsexp_ann_income = alt.Chart(df, 
        title="Annual Income by Sex and Years of Experience").mark_rect().encode(
        x='sex:N',
        y='annlabinc:Q',
        color='yrsexp:Q'
    ).properties(
        width=400,
        height=400
    )
    gender_yrsexp_ann_income = gender_yrsexp_ann_income.configure_title(fontSize=28)


def main():
    # Read in CSV datasets and clean up
    psid = pd.read_csv('../datasets/PanelStudyIncomeDynamics.csv',
            usecols=['sex', 'annlabinc', 'yrsexp', 'degree', 'hisp', 'black', 'white', 'age'])
    df = psid.dropna()
    gp = pd.read_csv('../datasets/GenderPay.csv',
            usecols=['Gender', 'BasePay', 'Bonus', 'Education', 'JobTitle', 'Dept'])
    gp = gp.dropna()
    alt.data_transformers.disable_max_rows()

    # Research question #1:
    gender_base_pay_bar(gp)
    gender_annual_income_pie(df)
    gender_bonus_pay_bar(gp)

    # Research question #2:
    ann_income_degree_bar(df)
    base_pay_education_level(gp)

    # Research question #3:
    job_cat_gender_bar(gp)
    job_dept_gender_bar(gp)

    # Research Question #4:
    ann_income_hisp(df)
    ann_income_black(df)
    ann_income_white(df)
    ann_income_age(df)
    ann_income_yrs_exp(df)


if __name__ == '__main__':
    main()
