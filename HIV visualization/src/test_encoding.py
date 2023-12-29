import get_data

data=get_data.scat3
data=data[['County','State','priority','hiv_rate','avg_nh_score']].copy()
print(data.loc[data['County']=="Washington"])

