import matplotlib.pyplot as plt
from scipy import stats
import copy
plt.style.use('dark_background')

# Dados

# Dados

def calcX(i:int):
   ii=[]
   for n in range(i):
       nn=[]
       xx=float(n)*0.1
       ii.append(copy.copy(xx))
       xx=float(n)*2.25
       ii.append(copy.copy(xx))
       
   return ii
def calcY(X):
    ii=[]
    counter=0
    for n in range(0,len(X),2):
        xx=X[n+0]+X[n+1]
        ii.append(copy.copy(xx))
        ii.append(copy.copy(xx))
    return ii

X=calcX(100)
y=calcY(X)
X80=X[:80]
X20=X[80:]
y80=y[:80]
y20=y[80:]
# Gráfico
plt.scatter(X80, y80, color="cyan")
plt.scatter(X20, y20, color="red")

plt.show()
