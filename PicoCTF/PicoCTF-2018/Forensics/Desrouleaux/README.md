Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell.picoctf.com 10493. [incidents.json](incidents.json)

# Solution
---
We have an incidents.json file, where inside a dictionary, we have some sessions.
We are supposed to use some python skills, needing to understand the concepts of dictionaries, sets... etc.
I did a [script](getflag.py) for getting the three answers in a row.
For the first question, we have to check which ip is the most repeated one.
For the second question, we have to get how many different ips where visited by a specific source ip address
For the third question, we have to get the average number of unique destionation ips a file hash is sent.

# Solución
---
Tenemos un archivo incidents.json, en el cual en dicho formato, tenemos un par de sesiones, las cuales tenemos que analizar y contestar una serie de preguntas.
Es muy sencillo de resolver con python, aunque hay que tener claros algunos conceptos como los diccionarios, sets, tuples... y saber cuál es más óptimo de usar.
La primera pregunta nos requiere el saber cual es la dirección IP que más se repite.
La segunda pregunta nos hace calcular por una dirección IP emisora en particular, teniendo que responder cuántas IP receptoras únicas (sin repetirse) hay.
La tercera pregunta es referente a calcular la media de direcciones únicas IP, que un archivo es enviado.
He hecho un [script](getflag.py) para resolver las 3 preguntas de 1.
