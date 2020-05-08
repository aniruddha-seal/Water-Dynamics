# The System has 884 Water Molecules
# Has a total of 501 Time Steps dumped after 0.2 ps 
import numpy as np
import MDAnalysis as md
import math
import scipy.optimize as sc
import matplotlib.pyplot as plt
u=md.Universe("/home/aniruddha/Desktop/Untitled Folder/frame_0.gro","/home/aniruddha/Desktop/Untitled Folder/fittraj.xtc")
N=len(u.trajectory)
print(N)
cutoff=int(N/5)
mut=np.zeros((N,3)) #Store Dipole Moment Vector
o=u.select_atoms("name OW") #O AtomGroups
hw1=u.select_atoms("name HW1") #HW1 AtomGroups
hw2=u.select_atoms("name HW2") #HW2 AtomGroups
corr=np.zeros((cutoff))#Storing Correlation Function
for ts in u.trajectory:
    for i in range(0,No_of_Molecule):
        dummy=o[i]+o[i]
        oc=dummy.center_of_geometry() #Position Vector of O
        dummy=hw1[i]+hw1[i]
        hw1c=dummy.center_of_geometry() #Position Vector of H1
        dummy=hw2[i]+hw2[i]
        hw2c=dummy.center_of_geometry() #Position Vector of H2
        mu=hw2c+hw1c-2*oc
        mu=mu/np.linalg.norm(mu) #Unit Vector along Dipole Moment
        mut[i]=mu
for ts in u.trajectory:
    for i in range(0,cutoff):
        if(ts.frame<N-i):
            x=ts.from_timestep(ts)
            for j in range(0,i):
                x=x.next()
            corr[i]=corr[i]+np.dot(mut[ts.frame],mut[x])
for i in range(0,cutoff):
    corr[i]=corr[i]/(N-i)
    corr[i]=0.5*(3*corr[i]-1) #Making 2nd Order Legendre Polynomial
#Drawing the OTCF graph
#print("x         y")
x=np.zeros((54000))
#file=open("OTCFDatamd_1_1.dat","a+")#File_object = open(r"File_Name","Access_Mode")
for i in range(0,N):
    x[i]=i
    #file.write(str(x[i]))
    #file.write("  ")
    #file.write(str(corr[i]))
    #file.write("\n")
#file.close()
ax = plt.subplot(111)
ax.plot(x,corr)
plt.axis([0,N,-0.25,1])
ax.set_xlabel("time step")
ax.set_ylabel("Orientational Time Corr Func")
ax.figure.savefig("OTCF_resid_XXXX.pdf")
plt.draw()
#Fitting to Multi Exponential Function
def model(x,a,b,k):
    return k*np.exp(-x/a)+(1-k)*np.exp(-x/b)
init_guess=[0.5,1,1]
fit=sc.curve_fit(model,x,corr,p0=init_guess)
ans,cov=fit
fit_a,fit_b,fit_k=ans
print(ans)
print(fit_k)
print(fit_a)
print(fit_b)
t=np.linspace(0,100)
plt.plot(t,model(t,fit_a,fit_b,fit_k))
plt.draw()
