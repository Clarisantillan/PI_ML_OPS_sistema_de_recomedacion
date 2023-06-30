import pandas as pd 
import numpy as np
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title='Sistema de Recomendacion de Peliculas',
            description='En este sitio podra ingresar diferentes parametros para obtener informacion sobre peliculas y directores')
templates = Jinja2Templates(directory="./index.html")
# creo ruta raiz http://127.0.0.1:8000

df_movies= pd.read_csv('./ETL/movies_limpio.csv')
df_actor=  pd.read_csv('./API/actor.csv')
df_director= pd.read_csv('./API/director.csv')

#index.html
#@app.get('/', response_class=HTMLResponse)
#def welcome(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request}) 

 
@app.get("/", response_class=HTMLResponse)
def root():
    return FileResponse("index.html", status_code=200)

#Funcion Filmaciones por Mes

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes):
    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }

    if mes.lower() in meses:
        numero_mes = meses[mes.lower()]
        cantidad_peliculas = obtener_cantidad_peliculas_mes(numero_mes)
        return f"{cantidad_peliculas} película(s) fueron estrenadas en el mes de {mes.capitalize()}."
    else:
        return "El mes ingresado no es válido."

# Función auxiliar para obtener la cantidad de películas estrenadas en x mes
def obtener_cantidad_peliculas_mes(numero_mes):
    cantidad_peliculas = len(df_movies[df_movies['release_month'] == numero_mes])
    return cantidad_peliculas


#Funcion Filmaciones por dia
@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia):
    dia=dia.lower()
    dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    
    if dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "jueves" or dia == "viernes" or dia == "sábado" or dia == "domingo":
        aux_dia = dias.index(dia)
        df_movies["release_date"] = pd.to_datetime(df_movies["release_date"])
        df_movies["release_day"] = df_movies["release_date"].dt.weekday
        resultado = df_movies.loc[df_movies["release_day"] == aux_dia].shape[0]
        return f"{resultado} película(s) fueron estrenadas en los días {dia.capitalize()}."  
    
    else:
        resultado = 'El día ingresado no es válido'
        return resultado 


#Funcion Titulo, Lanzamiento, Popularidad
@app.get('/score_titulo/{titulo_de_la_filmacion}')
def score_titulo(titulo_de_la_filmacion):
    titulos = df_movies['title']
    
    for titulo in titulos:
        if titulo == titulo_de_la_filmacion:
            fecha_series = df_movies[df_movies['title'] == titulo_de_la_filmacion]['release_year']
            popularidad_series = df_movies[df_movies['title'] == titulo_de_la_filmacion]['popularity']
            
            if not fecha_series.empty and not popularidad_series.empty:
                fecha = fecha_series.astype(str).iloc[0]
                popularidad = popularidad_series.astype(str).iloc[0]
                return f"La película {titulo.capitalize()} fue estrenada en el año {fecha} con una puntuación/popularidad de {popularidad}."
    
    return 'No se ha encontrado el título de la filmación'

#Funcion Votos de la filmacion
@app.get('/votos_titulo/{titulo_de_la_filmacion}')
def votos_titulo(titulo_de_la_filmacion) : 
    titulos = df_movies['title']
    
    for titulo in titulos:
        if titulo == titulo_de_la_filmacion:
            fecha_series = df_movies[df_movies['title'] == titulo_de_la_filmacion]['release_year']
            n_votos_series =  df_movies[df_movies['title'] == titulo_de_la_filmacion]['vote_count'].astype(int)
            promedio_series = df_movies[df_movies['title'] == titulo_de_la_filmacion]['vote_average']
            
            if not n_votos_series.empty and not fecha_series.empty and not promedio_series.empty:
                fecha = fecha_series.astype(str).iloc[0]
                n_votos = int(n_votos_series.astype(str).iloc[0])
                promedio= promedio_series.astype(str).iloc[0]
                
                if n_votos >= 2000:
                 return f"La película {titulo.capitalize()} fue estrenada en el año {fecha}. La misma cuenta con un total de {n_votos} valoraciones, con un promedio de {promedio}."
    
    return 'La filmacion no cuenta con suficientes votos para obtener la informacion solicitada.'



@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor) :
    nombres = df_actor['name']
    
    for nombre in nombres:
        if nombre == nombre_actor:
            contador= df_actor[df_actor['name'] == nombre_actor]['title'].shape[0]
            retorno_total = df_actor[df_actor['name'] == nombre_actor]['return'].sum().round(2)
            retorno_promedio = (retorno_total / contador).round(2)
            
        
            return f"El/la actor/a {nombre.capitalize()} ha recibido de {contador} filmaciones, un retorno de {retorno_total} con un promedio de {retorno_promedio} por filmación."
    
    return 'No se ha encontrado el actor solicitado.'


@app.get('/get_director/{nombre_director}')
def get_director(nombre_director):
    nombres = df_director['name']
    
    for nombre in nombres:
        if nombre == nombre_director:
            peliculas = (df_director[df_director['name'] == nombre_director]['title']).drop_duplicates()
            exito = (((df_director[df_director['name'] == nombre_director]['return']).drop_duplicates()).sum()).round(2)
            
        
            resultado = f"El director {nombre.capitalize()} ha obtenido un éxito de {exito}. Sus películas:\n"
            
            for i, pelicula in enumerate(peliculas):
                fecha_lanzamiento = df_director[(df_director['name'] == nombre_director) & (df_director['title'] == pelicula)]['release_date'].iloc[0]
                retorno = df_director[(df_director['name'] == nombre_director) & (df_director['title'] == pelicula)]['return'].iloc[0]
                costo = df_director[(df_director['name'] == nombre_director) & (df_director['title'] == pelicula)]['budget'].iloc[0]
                ganancia = df_director[(df_director['name'] == nombre_director) & (df_director['title'] == pelicula)]['revenue'].iloc[0]
                
                resultado += f"Película {i+1}: {pelicula}, lanzada el {fecha_lanzamiento} con un retorno de {retorno}. Sus costos={costo} USD y ganancias={ganancia} USD \n "
            
           
            
            return resultado
    
    return 'No se ha encontrado el director solicitado.'


@app.get('/recomendar_peliculas/{titulo_pelicula}')
def recomendar_peliculas(titulo_pelicula):
    df = pd.read_csv('./peliculas_filtradas.csv')
    num_similares = 5
    
    # Filtro el df por el título de la peli solicitada
    pelicula_filtro = df[df["title"] == titulo_pelicula]
    
    if pelicula_filtro.empty:
        print("No se encontró ninguna película con ese título.")
        return []
    
    # Obtengo el índice de la película filtrada
    target_movie_index = pelicula_filtro.index[0]

    # Creo las representaciones numéricas de las descripciones de películas
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["overview"])

    # Calculo la similitud del coseno entre las descripciones de películas
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Obtengo los índices de las películas más similares
    similar_movies_indices = similarity_matrix[target_movie_index].argsort()[::-1][1:num_similares+1]

    # Obtengo las películas similares del df
    peliculas_similares = df.iloc[similar_movies_indices]["title"].tolist()
    
    return f" Las peliculas similares para el titulo '{titulo_pelicula.capitalize()}' son:  {peliculas_similares}."
