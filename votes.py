import pandas as pd

def save_votes(prompt,winner):

    df=pd.read_csv('votes.csv')

    df.loc[len(df)]=[prompt,winner]

    df.to_csv("votes.csv",index=False)


