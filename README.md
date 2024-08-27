## Instrucciones para el funcionamiento
Para el correcto funcionamiento se debe realizar los siguientes pasos:
- Levantar el proyecto con ```sudo docker-compose up -d```
- Abrir en el navegador ```localhost:8001/docs``` y ```localhost:8002/docs```
- Ejecutar 1 prueba de ambos servicios de FastApi para demostrar su funcionamiento
- Dirigirse en el navegador a ```localhost:3000```, se mostrara la página de Grafana donde 
se debe iniciar sesión con usuario: ```admin``` y contraseña: ```admin```
- En el menú de Grafana ir a la opción de "Add Data Source" y agregar la opción de Loki con
la url ```http://loki:3100```
- Seleccionar la opción de Explore y revisar el correcto funcionamiento de los logs
- Para detener y eliminar los contenedores creados se debe ejecutar ```sudo docker-compose down```
