
PRACTICA_APRENDIZAJE_1

En este estudio hemos utilizado un conjunto de datos que incluye características de clientes y préstamos con el objetivo de explorar las variables más relevantes asociadas al riesgo de incumplimiento. Esto es, determinar qué características de los clientes están relacionadas con el incumplimiento de pagos en préstamos, utilizando técnicas de análisis exploratorio de datos (EDA) y preprocesamiento.

Para llevar a cabo este análisis hemos seguido la siguiente estructura:
En primer lugar hemos preprocesado los datos (Limpieza y preparación inicial, Revisión de duplicados y tratamiento de valores nulos), después hemos identificado variables relevantes (hemos verificado que las variables no incluyan información futura y hemos seleccionado variables como AMT_INCOME_TOTAL, NAME_CONTRACT_TYPE, CODE_GENDER, entre otras).
Hemos continuado con un análisis exploratorio (analizando la correlación de características como ingresos, género, estado civil y número de hijos con el incumplimiento (TARGET) y para finalizar hemos realizado la preparación para modelado (codificación de variables categóricas y tratamiento de valores extremos).

Hemos identificado patrones clave entre características como tipo de contrato, ingresos, y perfil demográfico con el incumplimiento de pagos. El conjunto de datos se compone de 5789 registros y 122 variables, destacando columnas como AMT_CREDIT, AMT_ANNUITY y EXT_SOURCE_1-3 por su relevancia en el análisis.

PRACTICA_DE_APRENDIZAJE_2

Este notebook se centra en el análisis y preprocesamiento de datos, preparando un conjunto para tareas de modelado predictivo, con especial atención a la variable objetivo TARGET. Se comenzó cargando el dataset pd.credit_procesado.csv y realizando una inspección preliminar que reveló un total de 307511 filas y 122 columnas. Las variables se clasificaron en categóricas (con menos de 50 valores únicos) y continuas, ajustando sus tipos de datos. Entre las categóricas se incluyeron variables como NAME_CONTRACT_TYPE, mientras que en las continuas destacaron variables como AMT_REQ_CREDIT_BUREAU_YEAR. El dataset se dividió de forma estratificada en conjuntos de entrenamiento (80%) y prueba (20%), asegurando que ambos mantuvieran la proporción de las clases de TARGET. 
En el análisis de valores nulos, se identificaron variables con altos porcentajes de datos ausentes, como aquellas relacionadas con indicadores crediticios. Para las variables numéricas, se generó una matriz de correlación de Pearson, destacando relaciones fuertes entre algunas variables como AMT_INCOME_TOTAL y AMT_CREDIT. Además, se realizó un análisis de outliers y se analizaron los valores nulos en función de la variable objetivo, observando diferencias significativas en la proporción de nulos entre las clases 0 y 1. Para las variables categóricas, se calcularon asociaciones utilizando la V de Cramer, destacando relaciones entre NAME_INCOME_TYPE y NAME_EDUCATION_TYPE. También se calculó el Weight of Association (WAO), identificando categorías con alta relevancia para la predicción de TARGET.

Finalmente, los datos preprocesados se exportaron en archivos CSV (pd.credit_procesado_train.csv y pd.credit_procesado_test.csv), dejando un conjunto limpio y estructurado, listo para análisis más avanzados o modelado predictivo.

PRACTICA_DE_APRENDIZAJE_3

Este notebook se centra en la codificación de variables categóricas y el escalado de datos para preparar el conjunto de datos de entrenamiento y prueba para modelado predictivo. Primero, se cargaron los datos procesados (data_train.csv y data_test.csv) y se separaron en características (X) y variable objetivo (target). Para la codificación de variables categóricas, se emplearon tres enfoques: (1) codificación manual para variables binarias como flag_own_car, transformando "Y" en 1 y "N" en 0; (2) One-Hot Encoding para variables con pocas categorías como name_contract_type y organization_type, generando nuevas columnas para cada categoría; y (3) Target Encoding para variables con muchas categorías, como occupation_type, reemplazando las categorías por la media de la variable objetivo. Una vez codificadas, las variables de X_test se alinearon con las de X_train para garantizar consistencia. Finalmente, las variables se escalaron utilizando StandardScaler, ajustando los datos de entrenamiento y aplicando el mismo escalado a los datos de prueba, asegurando que todas las características tuvieran media 0 y desviación estándar 1. Este proceso garantiza que los datos están correctamente preparados para su uso en modelos predictivos, maximizando la precisión y eficacia del análisis.






