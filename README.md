# T1            POL SEDÓ MOTA
## EXERCICI 1:
----

Si considerem la frequencia 4 KHz els 5 seguents persiodes serien aixi:
<img src="img/ex1_5T.png" width="480" align="center">
<br>

Guardem el so en un fitxer anomenat: `so_1.wav`
<br>
El modul i la fase daquests 5 periodes es el seguent:
<img src="img/TF_so1.png" width="480" align="center">
<br>

---

Ara repetim pero amb una 
* ### Fy=1000Hz
<img src="img/5T_so2.png" width="480" align="center">
<br>

Guardem al fitxer ``so_2.wav``
<img src="img/TF_so2.png" width="480" align="center">
<br>

### OBSERVEM:
Quan baixem la frequencia del to a 1k podem veure com els pics dels periodes no estan tan marcats

El modul de la transformada en canvi, ens mostra dos pics principals a la frquencia 1000 i 7000 

## EXERCICI 2:
-----

En aquests segon exercici comencem llegint el fitxer que hem creat anteriorment ``so_1.wav`` el qual conte el to sinusoidal anterior de frequencia 4Khz

Per aconseguir saber aquesta frequencia apartir del fitxer fem el seguent:
``` python
x_r, fm = sf.read('so_1.wav')
magspec = plt.magnitude_spectrum(x_r, fm)
fxx=magspec[1][np.argmax(magspec[0])]
print(f'la frequencia fonamental del to es de "{fxx}"Hz')
```
aqui estem agafant el valor de frequencia a on es troba la delta mes alta de la transformada (fonamental)

<img src="img/freq.png" width="480" align="center">
<br>

el valor de la variable `` fxx `` hauria de ser 4000

Ara representem 5 periodes del to i la seva transformada:
<img src="img/2_5T.png" width="480" align="center">
<br>
<img src="img/2_TF.png" width="480" align="center">
<br>
### OBSERVEM:

 observem que els valors de la transformada i els periodes eson molt semblants als de l'exercici 1 ja que llegeix correctament

## EXERCICI 3:
---

En aquest cas l'execisi consisteix en representar el modul en dBs, tornem a repetir el primer apartat de l'exercici anterior
