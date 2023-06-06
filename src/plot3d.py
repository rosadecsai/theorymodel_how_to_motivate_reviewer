from scipy.stats import norm 
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
def getDifg(beta,c):
	low_e =2
	high_e =10

	e_values=[low_e, high_e]
	low_y = 5
	high_y = 20
	a_values= np.linspace(low_y,high_y,10)
	eta = 0.5
	mu= 1.5
	k1=0.85
	k2=1.5
	samples_y=10
	sigma_e = 1
	d=[]	
	for e in e_values:
		E_y_e = k1*e;
		sigma_y=sigma_e*k2
		sumatorio=0;
		a= E_y_e*1.5
		y = np.linspace(low_y,a,samples_y);
		for i in range(0,samples_y):
			sumatorio+=1 - norm.cdf(y[i], loc=E_y_e, scale=sigma_y) 
		
				
		print("Sumatorio ",sumatorio, "E(y|e)=",E_y_e)
		d.append(((1+eta)*E_y_e-eta*a-eta*(mu-1)*sumatorio));
	dif_g=(beta*(d[1]-d[0])-c)	
	
	return dif_g

beta_values =np.linspace(0,0.99,10)
c_values = np.linspace(0.5,2.5,10)
B,C=np.meshgrid(beta_values,c_values);

Z= getDifg(B,C);
		
fig = plt.figure(figsize=(12,12))
plt.rc('text', usetex=True)



ax = plt.axes(projection='3d')
ax.tick_params(axis='z', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='x', labelsize=16)
#ax.contour3D(B, C, Z, 50, cmap='binary')
ax.plot_surface(B, C, Z, rstride=1, cstride=1,cmap=cm.jet, edgecolor='darkred', linewidth=0.1)
ax.set_xlabel(r"$\displaystyle \beta$",fontweight='bold',fontsize=22)
ax.set_ylabel("c",fontweight='bold',fontsize=22)

ax.view_init(25,59)
ax.set_title(r"$\displaystyle \beta(g(\overline{e},a)-g(\underline{e},a))-c$",fontweight='bold',fontsize=18,pad=-54);
fig.savefig("fig4.png")
plt.show()	
