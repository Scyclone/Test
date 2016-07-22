import numpy as np
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('https://raw.githubusercontent.com/Scyclone/Test/master/loansData_clean.csv')

irate = df['Interest.Rate'].astype(float)
irate[np.isnan(irate)] = 0
loanamt = df['Amount.Requested']
loanamt[np.isnan(loanamt)] = 0
fico = df['FICO.Score']
fico[np.isnan(fico)] = 0
monthly_income = df['Monthly.Income']
monthly_income[np.isnan(monthly_income)] = 0

house_ownership = df['Home.Ownership']
#Couldn't find another loop mechanic that would handle the line below
house_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in house_ownership]


y = np.matrix(irate).transpose()

x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x3 = np.matrix(monthly_income).transpose()
x4 = np.matrix(house_ownership).transpose()


x = np.column_stack([x1, x2, x3, x4])
X = sm.add_constant(x)

model = sm.OLS(y, X)

f = model.fit()

print('Coefficients: ', f.params[0:2])
print('Intercept: ', f.params[2])
print('P-Values: ', f.pvalues)
print('R-Squared: ', f.rsquared)

