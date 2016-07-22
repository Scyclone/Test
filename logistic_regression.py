import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import math

df = pd.read_csv('https://raw.githubusercontent.com/Scyclone/Test/master/loansData_clean.csv')

intercept = [1] * len(df)
df['Intercept'] = intercept

ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']
ir = df['Interest.Rate']
ir = [1 if x < 12 else 0 for x in ir]
df['IR_TF'] = ir
X = df[ind_vars]
y = df['IR_TF']

logit = sm.Logit(y, X)
result = logit.fit()
coeff = result.params
print(coeff)

def logistic_function(FicoScore, LoanAmount, coeff):

    prob = 1 / (1 + math.exp(coeff[0] + coeff[2] * FicoScore + coeff[1] * LoanAmount))
    if prob > 0.7:
        p = 1
    else:
        p = 0
    return prob, p

prob = logistic_function(720, 10000, coeff)[0]
decision = logistic_function(720, 10000, coeff)[1]

## plotting: lets test different FICO score for 10,000 USD loan -- Took this one from what you had on your github :)
Fico = range(550, 950, 10)
p_plus = []
p_minus = []
p = []
for j in Fico:
    p_plus.append(1 / (1 + math.exp(coeff[0] + coeff[2] * j + coeff[1] * 10000)))
    p_minus.append(1 / (1 + math.exp(-coeff[0] - coeff[2] * j - coeff[1] * 10000)))
    p.append(logistic_function(j, 10000, coeff)[1])

plt.plot(Fico, p_plus, label='p(x) = 1/(1+exp(b+mx))', color='blue')
plt.hold(True)
plt.plot(Fico, p_minus, label='p(x) = 1/(1+exp(-b-mx))', color='green')
plt.hold(True)
plt.plot(Fico, p, 'ro', label='Decision for 10000 USD')
plt.legend(loc='upper right')
plt.xlabel('Fico Score')
plt.ylabel('Probability and decision, yes = 1, no = 0')
plt.show()
