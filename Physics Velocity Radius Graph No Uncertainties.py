import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.7329905,1.1688017,1.4849969,1.883676,2.363244,2.7228281,3.1221209,3.5220268,3.9216874,4.320857,4.6799507,5.040639,5.482584,5.8856797,6.288653,7.0568533,7.9052067,8.752579,9.478863,10.246204,11.13488,11.901854,12.749717,13.557871,14.287344,15.13901,15.950232,16.758877,17.526955,18.254711,19.10331,19.992353,20.84181,21.530594,22.420618,23.109035,23.998323,24.847658,25.576273,26.386023,27.154222,27.964094,28.813921,29.542412,30.432314,31.200884,31.968225,32.817436,33.626205,34.353104,35.20207,35.93142,36.901844])
y = np.array([44.781902,59.18528,70.86315,80.01302,89.16407,96.17328,104.35038,111.554726,119.14818,127.51984,135.30725,140.56548,145.24123,147.3872,149.72774,150.12807,151.69687,154.82211,157.55647,159.31865,161.08261,163.42845,165.77548,166.95459,164.63058,160.94649,157.26178,157.66269,158.25757,158.65729,159.83700,161.0173,160.83514,158.89964,158.52353,157.17169,157.96289,157.97528,157.01314,155.66307,156.06339,154.51877,153.75296,152.98537,152.8038,152.62045,154.38264,154.58958,154.79594,156.55754,157.1536,155.02414,155.4274])
plt.plot(x,y,"r")
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.axis([1,40,1,200])
plt.show()
