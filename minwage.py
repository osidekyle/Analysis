import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Minimum Wage Data.csv",encoding="latin")
df.to_csv("minwagedata.csv",encoding="utf-8")
df=pd.read_csv("minwagedata.csv")
act_min_wage=pd.DataFrame()

for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage=group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage[name]=group.set_index("Year")[["Low.2018"]]

issue_df=df[df["Low.2018"]==0]
min_wage_corr=act_min_wage.replace(0,np.NaN).dropna(axis=1).corr()

for problem in  issue_df["State"].unique():
    if problem in min_wage_corr.columns:
        print("Something missing here")

grouped_issues=issue_df.groupby("State")
for state,data in grouped_issues:
    if data["Low.2018"].sum() !=0.0:
        print("Found some date for",state)



dfs=pd.read_html("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")
state_abv=dfs[0]
state_abv[["State/District","Postal Code"]].to_csv("stateabbv.csv",index=False)
state_abv=pd.read_csv("stateabbv.csv")
abbv_dict=state_abv.to_dict()
labels=[abbv_dict["Postal Code"][c] for c in range(len(min_wage_corr.columns))]
fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)



plt.show()

