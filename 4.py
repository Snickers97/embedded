import scipy.io as sci
import matplotlib.pyplot as plt
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
