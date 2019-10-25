# CNYT-Teoria-Cuantica-Basica


### Prerrequisitos:
 - Tener instalado python 3.7 o versiones mayores
 - Tener instalada la distribución de anaconda o en su defecto numpy y matplotlib.
 - Mantener el archivo complejos.py en la carpeta donde quiera ejecutar el archivo experimentos.py
 
### Contenido:
 - Función para hallar las probabilidades de hallar una particula en dererminadas posiciones de una recta
   ```
   particula_en_una_recta(n, vi):
    """
    Retorna un vector de probabilidades P.
    Parametros:
        n: Número de puntos sobre la recta.
        vi: Vector de estado inicial.
    """
   ```
 - Función para hallar las estadisticas de un observable:
   ```
    estadisticas_observables(o, vi):
    """
    Retorna el valor eperado E y la varianza S del observable
    Parametros:
        o: observable.
        vi: vector de estado inicial.
    """
   ```
 - Función para hallar los valores propios y el vector propio de un observable:
   ```
    valores_vectores_propios(observable, vi):
    """
        observable: observable del que se quieren obtener los valores propios y vectores propios
        vi: vector de estado inicial (ket)
    """
   ```
### Instalacion de la Libreria

Descargue el repositorio y almacene todos los archivos descargados en un solo paquete
Si tiene git use:
	```
		git clone https://github.com/D4v0r/CNYT-Teoria-Cuantica-Basica
	```

Si no, use las herramientas que la plataforma github le ofrece para descargar este repositorio.
Guarde esta carpeta en un lugar confiable y ejecute el archivo pruebas.py para verificar el funcionamiento de esta libreria

### Ejecucion de Pruebas
En la consola de su equipo  diririjase al path donde se encuentra guardada la libreria, un **ejemplo en la consola de WINDOWS** a continuacion:
	```
		cd C:\Users\Usuario\Downloads\CNYT>
	```
Para ejecutar las pruebas asegurese de tener python instalado y puesto en el **path** de su computador, ejecute el siguiente comando (EN WINDOWS):

	```
		py funciones_test.py
	```
Si estas arrojan un error de compilacion o algo por el estilo consulte la version de python  y en que sistema operativo(SO) esta corriendo las pruebas
 
 

### Acerca De
 
   - Universidad: Escuela Colombiana de Ingenieria Julio Garavito.
   - Curso: CNYT(Ciencias Naturales y Tecnología)
   - Grupo: 3
   - Proyecto 4

 
 Texto guia: QUANTUM COMPUTING FOR
COMPUTER SCIENTISTS.  


### Autor: Davor Cortés
### 2019-2
