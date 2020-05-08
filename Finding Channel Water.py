#Replace 54700 by the Total No of Frames in the Trajectory
import MDAnalysis as md
import numpy as np
import matplotlib.pyplot as plt
u=md.Universe("/home/kankana/Desktop/frame_0.gro","/home/kankana/Desktop/ordered.xtc")
chw=u.select_atoms("resname SOL and prop z< 65 and prop z>37 and (around 3 resid 27 or around 3 resid 32 or around 3 resid 36 or around 3 resid 39 or around 3 resid 57 or around 3 resid 60 or around 3 resid 61 or around 3 resid 64 or around 3 resid 116 or around 3 resid 109 or around 3 resid 112 or around 3 resid 239 or around 3 resid 247 or around 3 resid 251 or around 3 resid 254 or around 3 resid 255 or around 3 resid 258 or around 3 resid 210)")
print(chw.n_atoms)
chw=u.select_atoms("resname SOL and prop z<65 and prop z>37 and (around 3 resid 60 or around 3 resid 61 or around 3 resid 64 or around 3 resid 116 or around 3 resid 109 or around 3 resid 112 or around 3 resid 251 or around 3 resid 11 or around 3 resid 255)")
x=np.zeros((54700))
y=np.zeros((54700))
i=0
file=open("Number_of_ChannelWater.dat","a+")
for ts in u.trajectory:
    chwt=u.select_atoms("resname SOL and prop z<65 and prop z>37 and (around 3 resid 60 or around 3 resid 61 or around 3 resid 64 or around 3 resid 116 or around 3 resid 109 or around 3 resid 112 or around 3 resid 251 or around 3 resid 11 or around 3 resid 255)")
    y[i]=chwt.n_atoms/3
    x[i]=ts.frame
    file.write(str(x[i])
    file.write("  ")
    file.write(str(y[i]))
    file.write("\n")
    print(x[i])
    i=i+1
file.close()
ax = plt.subplot(111)
ax.plot(x,y)
plt.axis([0,i,0,50])
ax.set_xlabel("TimeStep")
ax.set_ylabel("Number of Water Molecules")
ax.figure.savefig("NumberDen.png")
plt.draw()


# In[ ]:




