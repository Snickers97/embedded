import scipy.io as sci
import matplotlib.pyplot as plt
import statistics as stats
clocks = sci.loadmat('clocktime')
drift_rates = sci.loadmat('rho_solution')
rho = drift_rates['rho'][0]
t = []
#making the clock times easier to use
t.append(clocks['tref'][0])
t.append(clocks['t1'][0])
t.append(clocks['t2'][0])
t.append(clocks['t3'][0])
t.append(clocks['t4'][0])
t.append(clocks['t5'][0])
t.append(clocks['t6'][0])
t.append(clocks['t7'][0])

sum = 0
for x in rho:
    sum += abs(x)

rint = 0.5/sum
print('Resynchronization interval:',round(rint,3),'seconds')

#Calculates the difference between each clock and the average value,
#then returns an array of the differences to be applied to the clock times
def FTA(t):
    y = []
    size = len(t)
    for i in range(1,size): #don't do this for tref, so starting at 1
        x = []
        for j in range(0,size):
            a = t[j]-t[i]
            x.append(a)
        x.sort()
        #For now, just assuming that k == 1
        x.pop()
        x.pop(0)
        a = stats.mean(x)
        y.append(a)
    return y

interval = t[0][0]
for i in range(0,len(t[0])):
    if t[0][i] >= interval: #run this code at each resync interval
        x = []
        for j in range(0,len(t)):   #Create a 1D array of the clock values at rsync time
            x.append(t[j][i])
        y = FTA(x)  #Calculate differnce between each clock and true value, store in array y
        for j in range(1,len(t)):
            for k in range(i,len(t[0])):
                t[j][k] += y[j-1]   #Add y value for each clock to all remaining values in the big array
        interval = t[0][i]+rint

for i in range(0,len(t)):
    plt.plot(t[0],t[i],label='clock'+str(i))
plt.title('Internal Synchronization')
plt.xlabel('Reference clock (clock 0)')
plt.ylabel('Local clock')
plt.legend(loc='upper left')
plt.show()
