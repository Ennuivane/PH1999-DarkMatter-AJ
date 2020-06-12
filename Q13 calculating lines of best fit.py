import numpy as np

x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror = np.array([0.05,0.05,0.05,0.05,0.05])



print("This program will compare your guess of the line of best fit and produce a value, the lower the value, the more accurate your prediction.")
guess = float(input("Guess a number: "))

ansarray = ((y-(x*guess))**2)/(yerror**2)
ans = np.sum(ansarray)
print(ans)
