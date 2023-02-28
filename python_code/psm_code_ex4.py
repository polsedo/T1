import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft
import tkinter
from tkinter import ttk 

f_AUDIO = 'September_EWF_mono.wav'
x_r, fm = sf.read(f_AUDIO)
print(f'la frequencia de mostreix del fitxer {f_AUDIO} es de "{fm}"Hz')
print(f'te un total de {len(x_r)} mostres')

T= 1.85                                 # Inici del segment
T2=1.875                                # final del segment
L = int(fm * T)
L2 = int(fm * T2)  
Ls = L2 - L                    # Nombre de mostres del senyal digital

Tm=1/fm                                 # Període de mostratge
t=Tm*np.arange(L,L2) 

sd.play(x_r, fm) 


plt.figure(1)
plt.plot(t,x_r[L:L2])
plt.xlabel('t en segons') 
plt.title('Exercici 4')
plt.show()

N=fm                                # Dimensió de la transformada discreta
X=fft(x_r[L : L2], N)  
k=np.arange(N)                        # Vector amb els valors 0≤  k<N


Xdb=20*np.log10(np.abs(X)/max(np.abs(X)))
Fk=(k/N)*(fm)

plt.figure(2)
plt.subplot(211)
plt.plot(Fk[0:int(fm/2)], Xdb[0:int(fm/2)])
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()

aviso=tkinter.Tk()
W1= ttk.Label(aviso, text='Estas escoltant September de Earth Wind and Fire')
W1.grid(column=0, row=1,padx=50,pady=50)
W1.pack()
aviso.mainloop()


