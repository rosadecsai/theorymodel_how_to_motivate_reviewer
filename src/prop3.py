from scipy.stats import norm 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
#increase the distance between E(y|\underline(e)) and E(y|\overline(e))
#Target: see how change the difference g(\overline(e),a)-g(\underline(e),a)
beta=0.175
c=1.25
low_e =2 #2,2
high_e =10 #10,20

e_values=[low_e, high_e]
low_y = 5
high_y = 20

eta = 0.5
mu= 1.5
k1=0.85
k1_sup=1.2
k2=1.5
dif_g=[]
dif_e=[]
samples_y=10
sigma_e = 1

for k1_sup in [1,1.2,1.5,2,2.5,3,3.5,4,4.5,5]:
	d=[]	
	pos=0;
	media_low=0;
	media_high=0
	for e in e_values:
		if (pos==0):
			E_y_e = k1*e;
			media_low=E_y_e
		else:
			E_y_e = k1_sup*e;	
			media_high=E_y_e;
		pos=(pos+1)	%2
		sigma_y=sigma_e*k2
	
		sumatorio=0;
		a= E_y_e*2
		y = np.linspace(low_y,a,samples_y);
		for i in range(0,samples_y):
			sumatorio+=1 - norm.cdf(y[i], loc=E_y_e, scale=sigma_y) 
		
				
		print("Sumatorio ",sumatorio, "E(y|e)=",E_y_e)
		d.append(((1+eta)*E_y_e-eta*a-eta*(mu-1)*sumatorio));
	dif_g.append(beta*(d[1]-d[0])-c)	
	dif_e.append(media_high-media_low)
plt.rc('text', usetex=True)


MEDIUM_SIZE=26
LARGE_SIZE=32
SMALL_SIZE=24
plt.rc('font', size=SMALL_SIZE)   

plt.rc('axes', labelsize=MEDIUM_SIZE) 
plt.rc('axes', titlesize=MEDIUM_SIZE) 
plt.rc('xtick', labelsize=SMALL_SIZE)  
plt.rc('ytick', labelsize=SMALL_SIZE)  
fig = plt.figure(figsize=(10,8),dpi=300)
ax = fig.add_subplot(111)
ax.plot(dif_e,dif_g)
txt = r"$\displaystyle c= $"+str(c)+r"$\displaystyle~~ \beta= $"+str(beta)
ax.set_title(txt,fontsize=LARGE_SIZE)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.set_xlabel(r"$\displaystyle E(y|\overline{e})-E(y|\underline{e})$",fontweight='bold',fontsize=LARGE_SIZE)
ax.set_ylabel(r"$\displaystyle \beta(g(\overline{e},a)-g(\underline{e},a))-c$",fontweight='bold',fontsize=LARGE_SIZE);
txt="figura5/fig_c"+str(c)+"_b"+str(beta)+".png"
fig.savefig(txt)
#plt.show()	
