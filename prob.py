import collections
import matplotlib.pyplot as plt
import scipy.stats as stats

testlist = [1, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9, 9, 9, 9, 9, 10, 12, 14, 14, 15]

c = collections.Counter(testlist)

print(c)

count_sum = sum(c.values())

for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


fig = plt.figure(0)
fig.canvas.set_window_title('Box Plot for Test List')
plt.boxplot(testlist)
plt.show()

fig = plt.figure(0)
fig.canvas.set_window_title('Histogram for Test List')
plt.hist(testlist, histtype='bar')
plt.show()

fig = plt.figure()
fig.canvas.set_window_title('QQ Plot for Test List')
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show()
plt.figure()
