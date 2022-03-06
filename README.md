## About the project 
Proyecto creado con Poetry que utiliza herramientas de machine learning para predecir si un cliente potencial termina siendo un cliente real. Mediante peticiones http (POST) se pueden enviar datos al modelo y este predice si se convertirá en cliente o no.
Data set obtenido de: https://www.kaggle.com/ashydv/leads-dataset?select=Leads.csv

## Machine Learning estimators 
Para predecir si un cliente se convertirá en cliente o no se han probado diferentes modelos, Support Vector Machine, KNeighborsClassifier y LogisticRegression, siendo este último el que mayor porcentaje de éxito ha tenido en sus predicciones (72%).

Para el tratamiento de los datos se han seguido en gran medida las directrices del usuario de Kaggle Abdelrahman Soltan.

## Conclusiones
En este trabajo se pretendía obtener un porcentaje de acierto de al menos el 90%, por lo que no se han conseguido los objetivos mínimos por ahora. En futuras versiones se hará un tratamiento de los datos más preciso y se probarán nuevos modelos y ajustes.
