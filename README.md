# Sistema de Recomendacion de Peliculas

 Este proyecto se basa en posicionarse en el rol de un MLOps Engineer y crear un sistema de recomendación de películas basado en la similitud de contenido. Se toma la información de películas en nuestro archivero de datos, para identificar aquellas películas similares a las que el usuario elige. Complementariamente se debian crear 6 funciones con el fin de obtener informacion relevenate sobre peliculas y directores.

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

1 -Obtener la cantidad de peliculas estrenadas en un mes especifico.
2- Obtener la cantidad de películas estrenadas en un día específico.
3- Obtener el titulo, el año de estreno y el score de la pelicula introducida.
4- Obtener el título, la cantidad de votos y el valor promedio de las votaciones de aquellas que cuenten con mas de 2000 valoraciones. 
5- Obtener el exito de un actor medido con el retorno, la cantidad de peliculas en las que participo y el promedio del retorno.
6- Obtener el éxito de un director medido a través del retorno, el nombre de cada película dirigida con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

Para la construccion de la API utiilice el framework FastAPI, para la simplificacion del proceso. Ya que es moderno y de altorendimiento.
