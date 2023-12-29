import get_data
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Rates displayed are the number of cases per 100,000 population.

# pull data for 45+ and all ages from data.py file
all_df=get_data.all_df
filtered_df=get_data.filtered_df

# plot scatter plot of HIV rates all ages and just age 45+ to show feasiblity of using limited data set
sns.set_theme(style="ticks")


fig, ax = plt.subplots()
sns.scatterplot(
    y="state", x="Rates of Persons Living with HIV, 2020", data=all_df, ax=ax)
ax.tick_params(labelsize=8)  # set the font size of the axis labels
plt.xticks(rotation=90)  # rotate the x-axis labels
ax.set_xlim(0, 2250)  # filter down limits
# limit number of tick marks shown for readability
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
fig.set_size_inches(12, 6, forward=True)
fig.suptitle("Rates of HIV All Ages")
# plt.savefig('Rates of HIV All Ages.png')


fig, ax = plt.subplots()
sns.scatterplot(y="state", x="HIV aged 45+", data=filtered_df, ax=ax)
ax.tick_params(labelsize=8)  # set the font size of the axis labels
plt.xticks(rotation=90)  # rotate the x-axis labels
ax.set_xlim(0, 2250)
# limit number of tick marks shown for readability
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
fig.set_size_inches(12, 6, forward=True)
fig.suptitle("Rates of HIV Ages 45+")
# plt.savefig('Rates of HIV Ages 45+.png')

plt.show()
