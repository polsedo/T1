import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                               # Freqüència de la sinusoide
fy=1000
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
y = A * np.cos(2 * pi * fy * t)
sf.write('so_1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
sf.write('so_2.wav', y, fm)

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
Ty=1/fy                                   # Període del senyal
Lsy=int(fm*5*Ty)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
sd.play(x, fm) 

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()    
                            # Visualització de l'objecte gràfic.
sd.play(y, fm)

plt.figure(1)                             # Nova figura
plt.plot(t[0:Lsy], y[0:Lsy])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.

#sd.play(x, fm)                           # Reproducció d'àudio
#sd.play(y, fm) 

#Domini transformat
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
Y=fft(y[0 : Lsy], N) 

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

plt.figure(3)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(Y))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Lsy} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(Y)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()