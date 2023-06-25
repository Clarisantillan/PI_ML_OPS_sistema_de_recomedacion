import pandas as pd 
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from datetime import datetime

app = FastAPI(title='Sistema de Recomendacion de Peliculas',
            description='En este sitio podra ingresar diferentes parametros para obtener informacion sobre peliculas y directores')

# creo ruta raiz http://127.0.0.1:8000

df_movies= pd.read_csv('./ETL/movies_limpio.csv')
df_movies.info()

@app.get("/")

def index():
    return "Hola soy Clari"   
 
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