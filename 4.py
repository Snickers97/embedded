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
rint = round(rint,3)
print('Resynchronization interval:',rint,'seconds')

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
        y.append(t[i]+a)
    return y

x = [4.06,4.04,4.07,4.08,4.18,100,1000]
y = FTA(x)
print('Final:',y)
