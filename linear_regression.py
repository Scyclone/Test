import numpy as np
import pandas as pd
import statsmodels.api as sm


loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))


loansData['Interest.Rate'] = cleanInterestRate
loansData['Loan.Length'] = cleanLoanLength
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x[:3]))

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())