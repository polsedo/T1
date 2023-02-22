import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft
                          
x_r, fm = sf.read('so_1.wav')
magspec = plt.magnitude_spectrum(x_r, fm)
#print(np.mean(magspec.))
fxx=magspec[1][np.argmax(magspec[0])]
print(f'la frequencia fonamental del to es de "{fxx}"Hz')

T= 2.5  
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

N=fm                       # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(2)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()