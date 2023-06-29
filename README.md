# Sistema de Recomendacion de Peliculas

Este proyecto se basa en posicionarse en el rol de un MLOps Engineer y crear un sistema de recomendación de películas basado en la similitud de contenido. Se toma la información de películas en nuestro archivero de datos, para identificar aquellas películas similares a las que el usuario elige. Complementariamente se debia crear 6 funciones con el fin de obtener informacion relevenate sobre peliculas y directores.

### Los datos entregados estaban en formato .csv, los mismos se encontraban en su mayoria anidados, sin transformar, y no contaban con procesos automatizados para la actualización de nuevas películas. Por lo que afronte el desafio de la siguiente manera:

## Estructura del proyecto
En la carpeta ETL, cree dos notebook (uno para movies.csv, donde hay informacion sobre las peliculas. Y otro para credits.csv donde hay informacion sobre directores y actores). Cargue en cada uno los datos entregados para hacer el ETL (extracción, transformación y limpieza de los datos), usando las siguientes librerías de Python:
Numpy - Pandas - Json.

 - Para aquellas columnas anidadas utilice diferentes metodos. A la columna 'belongs_to_collection', la converti en diccionario y luego con una funcion itere cada uno para guardar el valor de 'name' en una lista llamanda collection.
En la columna 'genres' utilice una funcion lamba. En las columnas 'production_countries', 'production_companies' y 'spoken_languages', utilice una expresion regular para extraer el 'name', modificando directamente toda la columna.

- Modifiqué los valores nulos de los campos 'revenue' y 'budget' con 0
- El formato de la columna 'release_date'la modifique a  AAAA-mm-dd. En base a esta columna cree la columna 'release_yeaer', 'release_month' y 'release_day'. Con el fin de preparar la data para futuros analisis.
-Creamos la columna del retorno = ingresos/presupuesto('revenue'/'budget')
-Elimine columnas necesarias, filtre nulos, y elimine filas con mas de 15  valores Nan(15 ya que me parecio que menos podrian ser relevantes igual)

Para ver mas en detalle pueden acceder a la carpeta llamada ETL en el repositorio.

