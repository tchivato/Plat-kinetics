import math

tiempos=[]
actividad=[]
z=1
n=1
res_antiguo=0

print('Introducir valores de x (horas). Pulsar 0 cuando estén todos')
while 1:
    tiempos.append(float(input('x'+str(z)+': '))/24)
    z+=1
    if 0 in tiempos:
        tiempos.pop()
        break
    
print('\nIntroducir valores de y (CPM/g o %Actividad)')
for i in range(len(tiempos)):
    actividad.append(float(input('y'+str(i+1)+': ')))
print('\n...calculando...')

#Cálculo residuo para n,a,c dados
def residuo(n,a,c):
    global res
    res=0
    for t in tiempos:
        h=0            
        for i in range(0,n):
            h+=math.exp(-a*t)*((a*t)**i)*(n-i)/math.factorial(i)
        res+=(actividad[tiempos.index(t)]-(c*h/n))**2
    return res

#Cálculo iterativo del mejor par a,c para un n dado
def iteracion(n):
    global a,c
    for c in range(int(0.5*int(max(actividad))),2*int(max(actividad))):
        a=0.01
        while residuo(n,a+0.01,c)<residuo(n,a,c) or a==0:      
            a+=0.01           
        if res<residuo(n,a,c+1):
            return residuo(n,a,c)

while 1:
        iteracion(n)
        if res>res_antiguo and res_antiguo!=0:
            fin=input('Terminado')
        res_antiguo=res
        print('\nNº HITS: ',n,'\na: ',round(a,2), '     c: ',c, '\nRESIDUOS: ',round(res))
        print('SUPERVIVENCIA PLAQUETAR:',round(n/a,1),' días\n\n...calculando...\n')        
        n+=1




