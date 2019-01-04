# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
better_event = data['Better_Event'].value_counts().idxmax()
# print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[top_countries.shape[0]-1],axis=0,inplace=True)

def top_ten(df,col):
    country_list = []
    df_nlargest = df.nlargest(10,col)
    country_list = df_nlargest['Country_Name'].tolist()
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = [element for element in top_10_summer if element in top_10_winter if element in top_10]



# --------------
#Code starts here

# Subsetting Dataframes
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#print(top_df.head())
# Plotting bar graphs
# fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(15,10))

ax_1 = summer_df.plot.bar(x='Country_Name',y='Total_Summer')
ax_1.set_xlabel('Countries')
ax_1.set_ylabel('Medals')

ax_2 = winter_df.plot.bar(x='Country_Name',y='Total_Winter')
ax_2.set_xlabel('Countries')
ax_2.set_ylabel('Medals')

ax_3 = top_df.plot.bar(x='Country_Name',y='Total_Medals')
ax_3.set_xlabel('Countries')
ax_3.set_ylabel('Medals')

plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio']==summer_max_ratio,'Country_Name'].iloc[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio']==winter_max_ratio,'Country_Name'].iloc[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio']==top_max_ratio,'Country_Name'].iloc[0]


# --------------
#Code starts here
data_1 = data.drop(data.index[data.shape[0]-1])
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total'])
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points']==most_points,'Country_Name'].iloc[0]
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


