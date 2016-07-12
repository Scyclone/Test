import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()

# Unsure of how to show the comparison of what I discovered, it would appear that the median and bottom (25%) remained the same,
# but there was a higher (75%) top box for amount requested vs the amount provided from Investors.
