# Interfaz Web - Reto de Predicción de Ventas en Favorita Ecuador
Interfaz web para generar predicciones en base a un modelo previamente entrenado; la interfaz cuenta con atributos de entrada, como lo son el número de tienda, la familia del producto y la fecha en la que se quieren calcular ventas. Se utilizan distintos atributos para generar predicciones, los cuales son calculados con los pares de senos y cosenos de los datos en el dominio de la frecuencia, además de realizar cálculos sobre los días festivos, fines de semana, y días de paga.

## Archivos
### main.py
Archivo de código que inicializa el servidor de Flask, también define el comportamiento que tendrá nuestra aplicación. Esto lo hace por medio de rutas y funciones que permiten navegar por distintas direcciones de la interfaz web y generar ciertos requests o cálculos con distintos atrinutos.

### index.html
En este archivo se define la estructura y el contenido de la interfaz web que se mostrará, se tienen bloques de interacción con el usuario, forms, para obtener los datos por los que se debe de filtrar la información de las predicciones.

### modelo_reto.sav
Modelo pre entrenado en formato sav, se utiliza la librería joblib para leer el archivo y generar predicciones con el modelo.

### datasets.zip
Dentro de esta carpeta comprimida se encuentran dos datasets importantes para la ejecución del código, ya que con este se cargan datos sobre la entrada de datos a la predicción y las columnas necesarias para formatear el DataFrame correspondiente a las predicciones.
