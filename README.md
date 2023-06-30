# Sistema de Recomendacion de Peliculas
 Este proyecto se basa en posicionarse en el rol de un MLOps Engineer y crear un sistema de recomendación de películas basado en la similitud de contenido. Se toma la información de películas en nuestro archivero de datos, para identificar aquellas películas similares a las que el usuario elige. Complementariamente se debian crear 6 funciones con el fin de obtener informacion relevante sobre peliculas y directores.

 Los datos entregados estaban en formato .csv, los mismos se encontraban en su mayoria anidados, sin transformar, y no contaban con procesos automatizados para la actualización de nuevas películas. Por lo que afronte el desafio de la siguiente manera:

## Estructura del proyecto
### ETL

En la carpeta ETL, cree dos notebook (uno para movies.csv, donde hay informacion sobre las peliculas. Y otro para credits.csv donde hay informacion sobre directores y actores). Cargue en cada uno los datos entregados para hacer el ETL (extracción, transformación y limpieza de los datos), usando las siguientes librerías de Python:
Numpy - Pandas - Json.

 - Para aquellas columnas anidadas utilice diferentes metodos. A la columna 'belongs_to_collection', la converti en diccionario y luego con una funcion itere cada uno para guardar el valor de 'name' en una lista llamanda collection.
En la columna 'genres' utilice una funcion lamba. En las columnas 'production_countries', 'production_companies' y 'spoken_languages', utilice una expresion regular para extraer el 'name', modificando directamente toda la columna.
- Reemplace los valores nulos de los campos 'revenue' y 'budget' con 0.
- Modifique formato de la columna 'release_date' a (AAAA-mm-dd). En base a esta columna cree la columna 'release_yeaer', 'release_month' y 'release_day'. Con el fin de preparar la data para futuros analisis.
- Cree la columna del retorno = ingresos/presupuesto('revenue'/'budget').
- Elimine columnas necesarias, filtre nulos, y elimine filas con mas de 15  valores Nan(15 ya que me parecio que menos podrian ser relevantes igual).

Para ver mas en detalle pueden acceder a la carpeta llamada ETL en el repositorio.

### API
Del ETL realizado, exporte los datos limpios a nuevos csv que utilice para desarrollar con exito las funciones solicitadas. Estas como mencione al principio, permiten al cliente obtener informacion relevenate sobre peliculas y directores. Enumero a continuacion la funcionalidad de de cada una:

1. Obtener la cantidad de peliculas estrenadas en un mes especifico.
2. Obtener la cantidad de películas estrenadas en un día específico.
3. Obtener el titulo, el año de estreno y el score de la pelicula introducida.
4. Obtener el título, la cantidad de votos y el valor promedio de las votaciones de aquellas que cuenten con mas de 2000 valoraciones. 
5. Obtener el exito de un actor medido con el retorno, la cantidad de peliculas en las que participo y el promedio del retorno.
6. Obtener el éxito de un director medido a través del retorno, el nombre de cada película dirigida con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
   
Para la construccion de la API utiilice el framework FastAPI, para la simplificacion del proceso. Ya que es moderno y de alto rendimiento.
El paso a paso de la creacion de las funciones y el merge entre los dataset se encuentra en la carpeta API y en main.py las funciones pasadas en limpio. 

### EDA
El siguiente paso fue realizar el analisis exploratorio de los datos(EDA).
En el pude observar estadisticas descriptivas, estructura de los datos y visualizacion de los datos faltantes(algo a destacar es que collection quedo con 42128 valores nulos, pero esto se debe a que al desglosar la columna 'belongs_to_collection' varias filas se asignan vacias ya que este es un diccionario que indica a que franquicia o serie de películas pertenece tal película y no todas pertenecen a una coleccion).

Tambien hice un recuento de los generos y procedi haciendo un analisis exploratorio profundo que incluye: Visualizacion de las relaciones entre variables, la distribucion de géneros, correlaciones, visualizacion del top 5 años de mayor cantidad de peliculas estrenadas, las productoras más frecuentes, directores con mayor numero de peliculas producidas, valores atipicos con boxplot, etc.
Las librerias que utilice para este punto: pandas, numpy, matplotlib y seaborn.
POdran ver el detalle del analisis en el archivo 'eda.ipynb'

### Sistema ML
Para crear mi sistema de recomendación de películas, utilicé una técnica llamada TfidfVectorizer. Esta técnica me permitió convertir las descripciones de las películas en representaciones numéricas, lo que facilita el cálculo de similitudes entre ellas.

En primer lugar, recopilé un conjunto de descripciones de películas obtenidas del ETL(por capacidad en render tuve que acotar la muestra a 3000 datos). Luego, utilicé el TfidfVectorizer para procesar estas descripciones. El TfidfVectorizer asigna un valor numérico a cada palabra en función de su importancia en el contexto del conjunto de descripciones. Las palabras más comunes en todas las descripciones, como "el" o "la", reciben un valor bajo, mientras que las palabras más distintivas y relevantes obtienen valores más altos.

Una vez que todas las descripciones se convirtieron en representaciones numéricas, utilicé la similitud del coseno para medir cuánto se parecen entre sí. La similitud del coseno es una medida que cuantifica la similitud entre dos vectores numéricos. En este caso, los vectores numéricos representan las descripciones de las películas.

Al calcular la similitud del coseno entre todas las descripciones de las películas, pude determinar qué películas eran más similares en términos de contenido. Esto me permitió recomendar películas similares a los usuarios en función de sus preferencias. Si un usuario disfrutó de una película en particular, podría recomendarle películas con descripciones similares utilizando el sistema de recomendación que construí.
Las librerias que utilice para este punto: pandas y sklearn.
El desarrollo de la funcion la pueden ver en el archivo 'ml.ipynb' y en el archivo main.py se utiliza para que sea visible en render.

### IMPLEMENTACION DEL PROYECTO
Para el deploy del mismo use el servicio Render. 
- Link al sitio: (https://sistema-de-recomedacion-peliculas.onrender.com)
- Link a video explicativo en Youtube: ()


