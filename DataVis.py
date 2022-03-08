import pandas as pd
import altair as alt
import numpy as np
import altair_viewer as av
import vega_datasets as vd

# Chart 1
# Bar chart: annual income grouped by sex based on degree level achieved
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'degree'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

# sex by annual income and degree level obtained
bar = alt.Chart(df, title="Annual Income by Sex and Degree Obtained").mark_bar().encode(
    x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
    y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
    color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"), scale=alt.Scale(scheme='darkmulti')),
    column=alt.Column('degree:O', title="Degree Levels (0=No College Degree, 1=Bachelor's, 2=Advanced)"),
).properties(
    width=200,
    height=700
)

bar.configure_title(fontSize=28)

# Chart 2
# Bar chart: annual income, sex, Hispanic
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'white', 'black', 'hisp'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

# Hispanic by annual income and sex
bar = alt.Chart(df, title="Annual Income Hispanic and Sex").mark_bar().encode(
    x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
    y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
    color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"), scale=alt.Scale(scheme='darkmulti')),
    column=alt.Column('hisp:O', title="Hispanic (0=No, 1=Yes)"),
).properties(
    width=200,
    height=700
)

bar.configure_title(fontSize=28)


# Chart 3
# Bar chart: annual income, sex, Black
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'white', 'black', 'hisp'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

# race by annual income and sex
bar = alt.Chart(df, title="Annual Income Black and Sex").mark_bar().encode(
    x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
    y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
    color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"), scale=alt.Scale(scheme='darkmulti')),
    column=alt.Column('black:O', title="Black (0=No, 1=Yes)"),
).properties(
    width=200,
    height=700
)

bar.configure_title(fontSize=28)

# Chart 4
# Bar chart: annual income, sex, White
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'white', 'black', 'hisp'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

# race by annual income and sex
bar = alt.Chart(df, title="Annual Income White and Sex").mark_bar().encode(
    x=alt.X('sex:N', axis=alt.Axis(title='Sex (1=Male, 2=Female)')),
    y=alt.Y('annlabinc:Q', axis=alt.Axis(title='Annual Income in USD')),
    color=alt.Color('sex:N', legend=alt.Legend(title="Sex by Color"), scale=alt.Scale(scheme='darkmulti')),
    column=alt.Column('white:O', title="White (0=No, 1=Yes)"),
).properties(
    width=200,
    height=700
)

bar.configure_title(fontSize=28)


# Chart 5
# Pie Chart: female vs male annual income
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'yrsexp'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

circle = alt.Chart(df, title="Male vs. Female Annual income").mark_arc().encode(
    theta=alt.Theta(field="annlabinc", type="quantitative"),
    color=alt.Color(field="sex", type="nominal"),
)
circle.configure_title(fontSize=28)


# Chart 6
# Heatmat: Annual Income by Sex and Years of experience
psid = pd.read_csv('PanelStudyIncomeDynamics.csv', usecols= ['sex', 'annlabinc', 'yrsexp'])

df = psid.dropna()
alt.data_transformers.disable_max_rows()

heat = alt.Chart(df, title="Annual Income by Sex and Years of Experience").mark_rect().encode(
    x='sex:N',
    y='annlabinc:Q',
    color='yrsexp:Q'
).properties(
    width=400,
    height=400
)

heat.configure_title(fontSize=28)