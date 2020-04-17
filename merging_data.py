import pandas as pd
import numpy as np

unemp_county=pd.read_csv("unemployment-by-county-us\output.csv")


df=pd.read_csv("Minimum Wage Data.csv",encoding="latin")
act_min_wage=pd.DataFrame()

for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage=group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage[name] = group.set_index("Year")[["Low.2018"]]
act_min_wage=act_min_wage.replace(0,np.NaN).dropna(axis=1)


def get_min_wage(year, state):
    try:
        return act_min_wage.loc[year][state]
    except:
        return np.NaN
unemp_county['min_wage'] = list(map(get_min_wage, unemp_county['Year'], unemp_county['State']))





pres16=pd.read_csv("2016uspresidentialvotebycounty\pres16results.csv")
top_candidates=pres16.head(10)['cand'].values

county_2015 =unemp_county[(unemp_county["Year"]==2015) & (unemp_county["Month"]=="February")]
state_abbv=pd.read_csv("stateabbv.csv",index_col=0)
state_abbv_dict=state_abbv.to_dict()["Postal Code"]
county_2015['State'] = county_2015['State'].map(state_abbv_dict)


pres16.rename(columns={"county":"County","st":"State"},inplace=True)


for df in pres16,county_2015:
    df.set_index(["County","State"], inplace=True)

pres16=pres16[pres16['cand']=="Donald Trump"]
pres16=pres16[['pct']]
pres16.dropna(inplace=True)

all_together = county_2015.merge(pres16, on=["County", "State"])
all_together.dropna(inplace=True)
all_together.drop("Year", axis=1, inplace=True)
print(all_together.corr())




