import numpy as np

x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror = np.array([0.05,0.05,0.05,0.05,0.05])


minchi2=10000
minslope=0.0
for slope in np.arange(0, 1, 0.0001):
    fx=slope*x
    chi2= np.sum(((y-fx)**2)/(yerror**2))
    if(chi2<minchi2):
        minchi2=chi2
        minslope=slope
print(minslope)
