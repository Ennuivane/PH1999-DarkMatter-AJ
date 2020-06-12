import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.7329905,1.1688017,1.4849969,1.883676,2.363244,2.7228281,3.1221209,3.5220268,3.9216874,4.320857,4.6799507,5.040639,5.482584,5.8856797,6.288653,7.0568533,7.9052067,8.752579,9.478863,10.246204,11.13488,11.901854,12.749717,13.557871,14.287344,15.13901,15.950232,16.758877,17.526955,18.254711,19.10331,19.992353,20.84181,21.530594,22.420618,23.109035,23.998323,24.847658,25.576273,26.386023,27.154222,27.964094,28.813921,29.542412,30.432314,31.200884,31.968225,32.817436,33.626205,34.353104,35.20207,35.93142,36.901844])
m = np.array([123000000,307000000,497000000,701000000,1050000000,1450000000,2000000000,2930000000,3930000000,5110000000,6600000000,8490000000,11700000000,13700000000,15500000000,18700000000,21200000000,23000000000,24300000000,26200000000,27700000000,29000000000,30200000000,31400000000,32000000000,32500000000,32600000000,32900000000,33100000000,33400000000,34200000000,35300000000,36300000000,36900000000,36700000000,36500000000,36800000000,38100000000,39500000000,40800000000,42100000000,42800000000,43400000000,43800000000,44300000000,44400000000,44500000000,45100000000,45600000000,46700000000,47800000000,48600000000,49800000000])
y = np.sqrt(4.3*0.000001*m/x)
plt.plot(x,y)
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.axis([1,40,1,200])
plt.show()

