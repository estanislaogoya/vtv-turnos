# Te vas de viaje y necesitas sacar turno lo antes posible en la VTV?

Tene un poco de paciencia, que corriendo este script tenes chances de agarrar cuando se liberan turnos en las plantas cerca.

---


#### COMO CORRERLO

Primero ingresa 

1. Metete en https://vtvpba.minfra.gba.gob.ar/SolicitudTurno. 
- Click derecho -> "inspect" -> Tab "Network"
- Carga tus datos personales y selecciona distintas plantas. Para cada una, chequea el request "turnos_por_fechas.json?planta_id=" y guardate el ID.
- Carga los id's con los nombres en el archivo main.py
- Por las dudas, copiate la cookie y guardala en el archivo `.env` (ver abajo)
2. [OPCIONAL] Create un Bot en Telegram . Vas a necesitar el TOKEN para autenticarte, y el CHAT_ID para mandar los mensajes a ese thread. https://www.directual.com/lesson-library/how-to-create-a-telegram-bot
- Si queres mandar la notificación a TG, marca el SEND_TO_BOT=TRUE en el `.env`
3. Clonate este repo local.
4. Crea un archivo .env y completa las variables que se muestran abajo
5. Dale play 
```shell
python main.py
```


##### ARCHIVO DE ENTORNO .ENV
- TOKEN=
- CHAT_ID=
- MAX_DATE=23-12-2023
- COOKIE="_vtv_session=2KV1gYxH2g8jj7SP9iRx43qapNil9XwtuJ0gfoeupWUlQfhjADYvtP7WFeHhOnc4vrIdqZwNKGjldes%2Bxeoq4FLkPOl8ceQaLSqzo%2BCbFHmtsIo8POPzLtIpMsKOE8crSn%2FMk0ZCJrp5RW0J9XjRey53%2FzUq%2BR%2FQaK03EcWZ%2FahY0Je%2B9dWXchbYXHRra8h3lrsAIoVjC2tY%2F48iomGlnMGWJKs27dj3MGmljs08t3wbMe%2BZvhjk9DOxgTdbne3nlLIfNA8H8q17GQ7mR2uysdsB4vS7Ev8gQXew1Z3lauew6cz076fbN0oPZI8%3D--L2drFEgJ1MY5muMa--4fLJkMluk8hnwjQxmLzQeA%3D%3D"
- SLEEP_TIME_IN_SEC=60
- PATENTE=
- SEND_TO_BOT=


#### Build image if not done already
```shell
docker-compose build
```

#### Run services
```shell
docker-compose up
```
