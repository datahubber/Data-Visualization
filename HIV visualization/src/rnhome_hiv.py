import get_data
import matplotlib.pyplot as plt
import mpld3 as mpl
import seaborn as sns

#data = pd.read_csv("data/scat3.csv")
data=get_data.scat4

# Create a seaborn plot
sns.scatterplot(data=data,x='hiv_rate',y='nh_count',hue='priority')

labels_df1 = data.dropna(subset=["hiv_rate","nh_count"])
labels_df = labels_df1[["County","State"]].copy()
labels = labels_df.values.tolist()

# Convert the plot to an interactive plot
fig = plt.gcf()
mpl.plugins.connect(fig, mpl.plugins.PointLabelTooltip(fig.axes[0].collections[0],labels=labels))

# Show the interactive plot
mpl.show()
