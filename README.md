## CORRECIONES
Realizamos correcciones  en la transformación y limpieza de datos tomando en cuenta la retroalimentación que recibimos, esto con el fin de obtener mejores features para el entrenamiento de nuestros modelos.

# Análisis y Limpieza de Datos - Reto de Predicción de Ventas en Favorita Ecuador

Este repositorio contiene el código y los archivos necesarios para abordar el reto de predicción de ventas en Favorita Ecuador. El reto implica predecir las ventas de las diversas familias de productos vendidos en las tiendas Favorita en Ecuador. El conjunto de datos proporcionado incluye información de tiendas, productos, promociones, fechas, y otros atributos relevantes.

## Equipo

- Diego Díaz
- Carlos Ortega
- Eduardo González
- Jesús Miranda
- Hilda Beltrán

## Descripción del Código

El archivo `retoFinal.ipynb` contiene el código en Jupyter Notebook utilizado para la solución del reto, en este mismo se realiza la limpieza y transformación de datos, así como la selección de un modelo adecuado. Para encontrar el modelo adecuado se realizó una serie de pruebas modificando los modelos utillizados, así como los hiperparámetros de cada uno; se utilizaron datos de entrenamiento, prueba y validación para calcular métricas y realizar interpretaciones sobre las mismas. A continuación, se presentan los pasos clave realizados en el código:

1. **Extracción de Datos**: Se importaron las bibliotecas necesarias para extraer, transformar y visualizar los datos. Se cargaron los archivos CSV de los conjuntos de datos, que incluyen información de tiendas, ventas, promociones, precios del petróleo, días festivos y más.

2. **Limpieza de Datos**:
   - Se identificaron los valores NaN en los conjuntos de datos y se imprimió el recuento total de valores NaN para cada conjunto.
   - El conjunto `oil.csv` contenía valores NaN, por lo que se probó la interpolación lineal para rellenar los valores NaN en la columna de precios del petróleo. Al compararlo con un reemplazo de los datos faltantes con la media aritmética, se obtuvo un mejor resultado en cuanto a la desviación estándar, al final nos quedamos con la media.
   - Se reemplazaron los caracteres especiales y números en la columna de descripción del conjunto `holidays_events.csv`.

3. **Transformación de Datos**:
   - Se transformó el conjunto `holidays_events.csv` para manejar las categorías de días festivos y transferencias, de manera que se obtuvieran las fechas reales en las que se celebraron los días festivos.
   - Debido a la previa transformación, la columna 'transferred' ya no era de mucha utilidad, por lo que se decidió no tomarla en cuenta, ya que se hizo la relación del evento con su fecha transferida.
   - Se ajustaron las categorías de días festivos para unificar las categorías 'Additional' y 'Bridge' bajo la categoría 'Holiday', debido a que no hay un interés en hacer una distinción entre estos tipos de evento. Aunque se mantienen los tipos de 'Work Day' y 'Event'.
   - Se generaron variables dummy para los tipos de evento que se encontraban en el DataFrame, además genermos características determinísticas para capturar patrones estacionales, por lo que usamos expansión de Fourier.
   - Se generó una variable dummy para identificar cuándo la fecha sea mayor a 4, lo cual nos indica que es un día dentro del fin de semana.
   - Se generó un DataFrame con los datos del número de tienda, familia del producto, fecha y ventas, indexados por el número de tienda, familia del producto y fecha.
  
 4. **Selección y Configuración del Modelo**:
    - El primer modelo seleccionado y configurado fue un modelo híbrido entre dos modelos de Random Forest, el primer Random Forest busca detectar la estacionalidad en el modelo, mientras que el segundo identifica la serialidad.
    - Se optó por utilizar el segundo modelo seleccionado y configurado, en el que se utilizó solamente un algoritmo de Random Forest, en realidad con nuestros datos limpios y transformados se obtenía un buen score. A pesar de esto, se optó por utilizar técnicas de regularización y ajustes de hiperparámetros para obtener un mejor comportamiento del modelo. Se utilizó una función para evaluar el modelo con distintos parámetros y seleccionar los mejores. En este caso, se optó por modificar la cantidad de árboles (n_estimators) por un valor de 250, además de utilizar un max_depth (distancia de la raíz hacia la última hoja), en este seleccionamos un valor de 15.
   
5. **Evaluación del Modelo**
   - Se utiliza un set de train, test y validation para el modelo. En este caso nuestro DataFrame de train se divide en train y validation, en 80 - 20% respectivamente; mientras que los datos de test se asignan a test. Esto nos permite validar que el modelo está funcionando de manera correcta para predecir las ventas por tienda, familia del producto y fecha.
   - Se calcula el error RMSLE para encontrar overfitting o underfitting en el modelo.

6. **Refinamiento**
   - En este modelo no se utilizaron técnicas de regularización, debido a que es un modelo de Random Forest y este solo puede ser modificado por medio de los hiperparámetros que proporciona el modelo.
   - Los hiperparámetros que se modificaron fueron n_estimators para el número de árboles de decisión a utilizar, así como el max_depth que es la distancia máxima entre el nodo raíz y la última hoja del árbol. Con esto pudimos obtener un error más bajo para el desempeño del modelo.
    
 8. **Interfaz web**
- Se genera una interfaz web para desplegar el modelo y permitir que sea interactivo para el ususario. Este se encuentra en la carpeta 'web_interface', todos los archivos necesarios se encuentran en la carpeta.

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
