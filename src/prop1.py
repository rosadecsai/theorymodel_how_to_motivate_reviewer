from scipy.stats import norm 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
#Code for  fig1-fig3. 
#bias of the reviewer
beta=0.175
#cost of high effort
c=0.75
#effort low and high in the paper \underline{e} and \overline{e}
low_e =2
high_e =10
e_values=[low_e, high_e]

#range of the manuscript evaluation outcome y
low_y = 5
high_y = 20

#possibles goal in the date 0 
a_values= np.linspace(low_y,high_y,10)

# the weight attached to the gain from satisfying the goal and the loss
#from falling short of the goal.
eta = 0.5

#reviewer’s loss-aversion coefficien. It must be bigger than 1
mu= 1.5
#factor to get E(y|e) from the effort
k1=0.85
#factor of sigma_y from the effort's sigma 
k2=1.5
#We have supposed that the y follows a normal distribution 

dif_g=[]#memory to store the objective function \beta*(g(y|\overline{e})-g(y|\underline{e}))-c
samples_y=10
sigma_e = 1
for a in a_values:
	d=[]	
	for e in e_values:
		E_y_e = k1*e;
		sigma_y=sigma_e*k2
		#the integral of F(y|e) is approximated for a summation
		sumatorio=0;	
		#samples for y
		y = np.linspace(low_y,a,samples_y);
		for i in range(0,samples_y):
			sumatorio+=1 - norm.cdf(y[i], loc=E_y_e, scale=sigma_y) 
		
		print("Summation ",sumatorio, "E(y|e)=",E_y_e)
		d.append(((1+eta)*E_y_e-eta*a-eta*(mu-1)*sumatorio));
	dif_g.append(beta*(d[1]-d[0])-c)	
#plot the function
plt.rc('text', usetex=True)
MEDIUM_SIZE=26
LARGE_SIZE=34
SMALL_SIZE=24
plt.rc('font', size=SMALL_SIZE)   
plt.rc('axes', labelsize=MEDIUM_SIZE) 
plt.rc('axes', titlesize=MEDIUM_SIZE) 
plt.rc('xtick', labelsize=SMALL_SIZE)  
plt.rc('ytick', labelsize=SMALL_SIZE)  
fig = plt.figure(figsize=(10,8),dpi=300)
ax = fig.add_subplot(111)
ax.plot(a_values,dif_g)
txt = r"$\displaystyle c= $"+str(c)+r"$\displaystyle~~ \beta= $"+str(beta)
ax.set_title(txt,fontsize=LARGE_SIZE)
ax.set_xlabel("a",fontweight='bold',fontsize=LARGE_SIZE)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.set_ylabel(r"$\displaystyle \beta(g(\overline{e},a)-g(\underline{e},a))-c$",fontweight='bold',fontsize=26);
txt="figura3/fig_c"+str(c)+"_b"+str(beta)+".png"
fig.savefig(txt)

