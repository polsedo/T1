import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft
                          
x_r, fm = sf.read('so_2.wav')
magspec = plt.magnitude_spectrum(x_r, fm)
#print(np.mean(magspec.))
fxx=magspec[1][np.argmax(magspec[0])]
print(fxx)

T= 2.5  
fx=4000
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)     

Tx=1/fxx                                   # Període del senyal
Ls=int(fm*5*Tx)  
                
print("importado correctamente")

sd.play(x_r, fm) 


 
plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show() 