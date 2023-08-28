Aquí tienes un archivo README para el código y el conjunto de datos proporcionado:

# Análisis y Limpieza de Datos - Reto de Predicción de Ventas en Favorita Ecuador

Este repositorio contiene el código y los archivos necesarios para abordar el reto de predicción de ventas en Favorita Ecuador. El reto implica predecir las ventas de las diversas familias de productos vendidos en las tiendas Favorita en Ecuador. El conjunto de datos proporcionado incluye información de tiendas, productos, promociones, fechas, y otros atributos relevantes.

## Equipo

- Diego Díaz
- Carlos Ortega
- Eduardo González
- Jesús Miranda
- Hilda Beltrán

## Descripción del Código

El archivo `draft1.ipynb` contiene el código en Jupyter Notebook utilizado para limpiar y transformar el conjunto de datos proporcionado. A continuación, se presentan los pasos clave realizados en el código:

1. **Extracción de Datos**: Se importaron las bibliotecas necesarias para extraer, transformar y visualizar los datos. Se cargaron los archivos CSV de los conjuntos de datos, que incluyen información de tiendas, ventas, promociones, precios del petróleo, días festivos y más.

2. **Limpieza de Datos**:
   - Se identificaron los valores NaN en los conjuntos de datos y se imprimió el recuento total de valores NaN para cada conjunto.
   - Para el conjunto `oil.csv`, se probó la interpolación lineal para rellenar los valores NaN en la columna de precios del petróleo.
   - Se reemplazaron los caracteres especiales y números en la columna de descripción del conjunto `holidays_events.csv`.

3. **Transformación de Datos**:
   - Se transformó el conjunto `holidays_events.csv` para manejar las categorías de días festivos y transferencias, de manera que se obtuvieran las fechas reales en las que se celebraron los días festivos.
   - Se ajustaron las categorías de días festivos para unificar las categorías 'Additional' y 'Bridge' bajo la categoría 'Holiday'.

## Conjunto de Datos

El conjunto de datos proporcionado incluye varios archivos CSV con información sobre tiendas, productos, ventas, promociones, precios del petróleo y días festivos. La descripción de los archivos es la siguiente:

- `train.csv`: Datos de entrenamiento que incluyen series de tiempo de características como `store_nbr`, `family`, `onpromotion` y el objetivo de ventas `sales`.

- `test.csv`: Datos de prueba con las mismas características que los datos de entrenamiento. El objetivo es predecir las ventas para las fechas en este conjunto.

- `sample_submission.csv`: Archivo de muestra para enviar las predicciones en el formato correcto.

- `stores.csv`: Metadatos de las tiendas, incluyendo ciudad, estado, tipo y agrupación (cluster).

- `oil.csv`: Precios diarios del petróleo. Incluye valores durante el período de tiempo de los datos de entrenamiento y prueba.

- `holidays_events.csv`: Días festivos y eventos con metadatos. Prestar atención a la columna 'transferred' que indica si un día festivo fue trasladado oficialmente a otra fecha.

## Notas Adicionales

- Los salarios en el sector público se pagan cada dos semanas el día 15 y el último día del mes. Las ventas en los supermercados podrían verse afectadas por esto.
- Un terremoto de magnitud 7.8 afectó a Ecuador el 16 de abril de 2016. Los esfuerzos de ayuda afectaron las ventas en los supermercados durante varias semanas después del terremoto.