from scipy.optimize import curve_fit
import numpy as np
from scipy.special import factorial

#License
print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")
print("\nA program to calculate platelet survival time via multiple-hit method\nCopyright (C) 2021  Tomás Chivato Martín-Falquina\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\nany later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see https://www.gnu.org/licenses\n\nIcons made by Freepik from www.flaticon.com")
print("\n--------------------------------------------------------------------")
print("--------------------------------------------------------------------")

res_prev=0
n=1
days=()
cpm=()



#Data input
datapoints=input('\nNumber of data points: ')
print('Input x values (hours)')
for i in range(int(datapoints)):
    days=np.append(days,float(input('x'+str(i+1)+': '))/24)
    
print('\nInput y values (CPM/g)')
for i in range(int(datapoints)):
    cpm=np.append(cpm,float(input('y'+str(i+1)+': ')))



#Output of the multiple hit formula  
def func(x,a,c):
    h=0
    for i in range(0,n):
        h+=((np.exp(-a*x))*(n-i)*(a*x)**i)/factorial(i)
    return c*h/n



#Iteration loop. The n value is not included in the optimization, but checked sequentially until the best value is obtained
while 1:
    popt, pcov = curve_fit(func, days, cpm, bounds=((0, 0), (100, np.inf)))
    a=popt[0]
    c=popt[1]
    res=sum((cpm - func(days,a,c))**2)

    if res>res_prev and res_prev!=0:
        break

    result='\n\nPLATELET SURVIVAL TIME: '+str(round(n/a,1))+' days'+'\n\nNumber of hits: '+str(n)+'\na: '+str(round(a,3))+ '\nc: '+str(round(c))+ '\nResidual: '+str(round(res))
    n+=1
    res_prev=res 

print(result)        
end=input()
