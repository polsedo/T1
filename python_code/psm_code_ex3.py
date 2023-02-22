import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft


x_r, fm = sf.read('so_1.wav')
magspec = plt.magnitude_spectrum(x_r, fm)
#print(np.mean(magspec.))
fxx=magspec[1][np.argmax(magspec[0])]
T= 2.5  
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)     

Tx=1/fxx                            # Període del senyal
Ls=int(fm*5*Tx)
N=fm                                # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)  
k=np.arange(N)                        # Vector amb els valors 0≤  k<N


Xdb=20*np.log10(np.abs(X)/np.max(np.abs(X)))
Fk=(k/N)*(fm)

plt.figure(0)
plt.plot(Fk/2,Xdb)
plt.show()
