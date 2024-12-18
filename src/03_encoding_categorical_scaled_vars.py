# -*- coding: utf-8 -*-
"""03_encoding_categorical_scaled_vars

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15whgBVBAxKWgLq8Ok7Bl9_gP-VQiKqF4

# **Codificación de las variables categoricas, escalado y modelo**

## **Importo librerías**
"""

import pandas as pd
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

"""## **Lectura de datos del tratamiento de valores missing y outliers**"""

credit_tratado_train = pd.read_csv("credit_tratado_train.csv")
credit_tratado_test = pd.read_csv("credit_tratado_test.csv")

"""# **Borrar la celda de abajo, la de str lower una vez tengamos los datos buenos**"""

credit_tratado_train.columns = credit_tratado_train.columns.str.lower()
credit_tratado_test.columns = credit_tratado_test.columns.str.lower()

X_train = credit_tratado_train.drop('target', axis=1)
y_train = credit_tratado_train['target']
X_test = credit_tratado_test.drop('target', axis=1)
y_test = credit_tratado_test['target']

"""### **Codificación de Variables:**

Para codificar las variables categóricas, hemos utilizado tres enfoques distintos en función del tipo de variable y el número de valores únicos que contienen. A continuación, se explica cada uno de estos enfoques:



1.   Variables binarias (Sí/No):
Para las variables categóricas con solo dos posibles valores, como "Y" y "N" (por ejemplo, `flag_own_car`, `flag_own_realty`), hemos realizado una codificación manual. En este caso, hemos asignado el valor 1 a "Y" y el valor 0 a "N". De esta manera, las variables se transforman en valores numéricos binarios que son más fáciles de procesar por los modelos.



2.   Variables con pocas categorías (One-Hot Encoding):
Para las variables que contienen un número limitado de categorías, como `name_contract_type` o `fondkapremont_mode`, hemos utilizado One-Hot Encoding. Este método crea nuevas columnas binarias para cada categoría única de la variable. Dado que estas variables tienen un número reducido de valores únicos, el uso de One-Hot Encoding no genera un exceso de columnas, lo que lo convierte en una opción eficiente.

3. Variables con muchos valores únicos (Target Encoding):
En el caso de las variables con un número mayor de valores únicos, como `occupation_type` o `name_housing_type`, hemos optado por Target Encoding. Este enfoque reemplaza cada categoría con la media del valor de la variable objetivo (`target`) para esa categoría. Al tratarse de variables con muchas categorías, Target Encoding resulta más adecuado, ya que evita la expansión excesiva del número de columnas en el conjunto de datos, lo que podría ocurrir con One-Hot Encoding.

"""

credit_tratado_train

X_train

# Codifciacion X_train

X_train['flag_own_car'] = X_train['flag_own_car'].map({'Y': 1, 'N': 0})
X_train['flag_own_realty'] = X_train['flag_own_realty'].map({'Y': 1, 'N': 0})
X_train['emergencystate_mode'] = X_train['emergencystate_mode'].map({'Yes': 1, 'No': 0})

X_train = pd.get_dummies(X_train, columns=['name_contract_type', 'code_gender',
                                           'name_education_type', 'housetype_mode',
                                           'fondkapremont_mode', 'organization_type'])


target_encoder = TargetEncoder(cols=['name_type_suite', 'name_income_type',
                                     'occupation_type', 'wallsmaterial_mode',
                                     'name_family_status', 'name_housing_type',
                                     'weekday_appr_process_start'])

X_train = target_encoder.fit_transform(X_train, y_train)

# Codifciacion X_test

X_test['flag_own_car'] = X_test['flag_own_car'].map({'Y': 1, 'N': 0})
X_test['flag_own_realty'] = X_test['flag_own_realty'].map({'Y': 1, 'N': 0})
X_test['emergencystate_mode'] = X_test['emergencystate_mode'].map({'Yes': 1, 'No': 0})

X_test = pd.get_dummies(X_test, columns=['name_contract_type', 'code_gender',
                                           'name_education_type', 'housetype_mode',
                                           'fondkapremont_mode', 'organization_type'])

X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

X_test = target_encoder.transform(X_test)

"""### **Escalado de variables**"""

scaler = StandardScaler()

X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

X_train_scaled.describe()