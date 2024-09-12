import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2 Add an overweight column to the data. 
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3
# Normalize the data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, make the value 0. 
# If the value is more than 1, make the value 1.
# df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x <= 1 else 1)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt 
    # with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # do this instead 
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})
    

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using
    # the following method provided by the seaborn library import : sns.catplot()
    plot = sns.catplot(data=df_cat,
                      x='variable',
                      y='total',
                      hue='value',
                      col='cardio',
                      kind='bar')



    # # 8
    fig = plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # 12
    corr = df_heat.corr()


    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12,10))


    # 15

    sns.heatmap(
        corr,
        mask=mask, 
        annot=True, fmt=".1f", cmap='coolwarm', square=True, linewidths=.5)


    # 16
    fig.savefig('heatmap.png')
    return fig
