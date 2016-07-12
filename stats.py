import pandas as pd
import scipy.stats as stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

AlcoholMean = str(df['Alcohol'].mean())
TobaccoMean = str(df['Tobacco'].mean())

AlcoholMedian = str(df['Alcohol'].median())
TobaccoMedian = str(df['Tobacco'].median())

AlcoholMode = str(stats.mode(df['Alcohol']))
TobaccoMode = str(stats.mode(df['Tobacco']))

AlcoholRange = str(max(df['Alcohol']) - min(df['Alcohol']))
TobaccoRange = str(max(df['Tobacco']) - min(df['Tobacco']))

AlcoholVariance = str(df['Alcohol'].var())
TobaccoVariance = str(df['Tobacco'].var())

AlcoholStd = str(df['Alcohol'].std())
TobaccoStd = str(df['Tobacco'].std())


print("The means for Alcohol and Tobacco data sets respectively are: " + AlcoholMean + " and " + TobaccoMean)
print("The medians for Alcohol and Tobacco data sets respectively are: " + AlcoholMedian + " and " + TobaccoMedian)
print("The modes for Alcohol and Tobacco data sets respectively are: " + AlcoholMode + " and " + TobaccoMode)
print("The ranges for Alcohol and Tobacco data sets respectively are: " + AlcoholRange + " and " + TobaccoRange)
print("The variances for Alcohol and Tobacco data sets respectively are: " + AlcoholVariance + " and " + TobaccoVariance)
print("The standard deviations for Alcohol and Tobacco data sets respectively are: " + AlcoholStd + " and " + TobaccoStd)