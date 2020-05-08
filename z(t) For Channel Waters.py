#Replace 4000 by Number of Frames
import MDAnalysis as md
import numpy as np 
import matplotlib.pyplot as plt
u=md.Universe("/home/kankana/Desktop/frame_0.gro","/home/kankana/Desktop/tiny.xtc")
print(0)
c=u.select_atoms("resname SOL and prop z<65 and prop z>37 and (around 3 resid 60 or around 3 resid 61 or around 3 resid 64 or around 3 resid 116 or around 3 resid 109 or around 3 resid 112 or around 3 resid 251 or around 3 resid 11 or around 3 resid 255)")
for ts in u.trajectory:
    chwt=u.select_atoms("resname SOL and prop z<65 and prop z>37 and (around 3 resid 60 or around 3 resid 61 or around 3 resid 64 or around 3 resid 116 or around 3 resid 109 or around 3 resid 112 or around 3 resid 251 or around 3 resid 11 or around 3 resid 255)")
    dummy=c.union(chwt)
    c=dummy
    print(ts.frame)
chOW=c.select_atoms("name OW")
N=len(chOW)
y=np.zeros((N,4000))
x=np.zeros((4000))
file=open("z(t)forChannelWater.dat","a+")
for ts in u.trajectory:
    k=ts.frame
    x[k]=ts.frame
    file.write(str(k))
    file.write("  ")
    print(k)
    for i in range(0,N):
        dummy=chOW[i]+chOW[i]
        z=dummy.center_of_geometry()
        y[i,k]=z[2]
        file.write(str(y[i,k]))
        file.write("  ")
    file.write("\n")
file.close()
ax = plt.subplot(111)
for i in range(0,N):
    l=str(chOW[i])
    plt.plot(x,y[i],label=l)
    ax.plot(x,y[i],label=l)
plt.axis[0,k,0,100]
ax.set_xlabel("TimeStep")
ax.set_ylabel("Z(t)")
ax.legend()
ax.figure.savefig("Z(t).png")
plt.legend()
plt.show()

