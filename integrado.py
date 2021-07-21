import ISI_Py
import matplotlib.pyplot as plt
import numpy as np
import time
print(ISI_Py.__doc__)
nsteps=100000000
n=20
a,s,En,Mn=[],30,[],[]
h=np.linspace(0,3.5,s)
for i in h:
    TIEMPO=time.time()
    a.append(ISI_Py.isi(n,i,nsteps))
    print((time.time()-TIEMPO)/60," mins")
for f in a:
    Mn.append(f[0])
    En.append(f[1])
plt.plot(h,En,"s")
plt.plot(h,np.zeros((s,)),"--",color="gray")
plt.plot(h,Mn,"s")
plt.xlabel("KT/J",size=20)
plt.ylabel("E/N,M/N",size=20)
plt.annotate("E/N", xy=(2, -2.4), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
plt.annotate("M/N", xy=(2.4,-0.2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

plt.show()
