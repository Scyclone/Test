import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('https://raw.githubusercontent.com/bwilson668/thinkful/master/unit-2/LoanStats3a.csv', header=1, low_memory=False)

df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

print(year_month_summary)
print(loan_count_summary)

plt.plot(loan_count_summary)
#plt.show()

loan_cnt_sum_dif = loan_count_summary.diff()
loan_cnt_sum_dif = loan_cnt_sum_dif.fillna(0)

plt.plot(loan_cnt_sum_dif)
#plt.show()

sm.graphics.tsa.plot_acf(loan_cnt_sum_dif)
sm.graphics.tsa.plot_pacf(loan_cnt_sum_dif)
plt.show()

#Something tells me that I really screwed this one up lol