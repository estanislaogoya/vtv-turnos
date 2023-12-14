# Te vas de viaje y necesitas sacar turno lo antes posible en la VTV?

Tene un poco de paciencia, que corriendo este script tenes chances de agarrar cuando se liberan turnos en las plantas cerca.

---


## COMO CORRERLO LOCALMENTE

1. Metete en https://vtvpba.minfra.gba.gob.ar/SolicitudTurno. 
    - Click derecho -> "inspect" -> Tab "Network"
    - Carga tus datos personales y selecciona distintas plantas. Para cada una, chequea el request en la tab network que arranca `turnos_por_fechas.json?planta_id=` y guardate el `ID`.
    - Carga los id's con los nombres de las plantas para tener como referencia en el archivo `main.py`
    - Por las dudas, copiate la cookie y guardala en el archivo `.env` (ver abajo)
2. [OPCIONAL] Create un Bot en Telegram . Vas a necesitar el TOKEN para autenticarte, y el CHAT_ID para mandar los mensajes a ese thread. https://www.directual.com/lesson-library/how-to-create-a-telegram-bot
    - Si queres mandar la notificación a TG, marca el SEND_TO_BOT=TRUE en el `.env`
3. Clonate este repo local.
4. Instala dependencias, por las dudas -> `pip install -r requirements.txt`
5. Crea un archivo .env y completa las variables que se muestran abajo
    - Modifica MAX_DATE para la fecha que vos quieras buscar como máximo. Solo te va a alertar si encuentra un turno antes de esa fecha.
6. Dale play 
```shell
python main.py
```


## ARCHIVO DE ENTORNO .ENV
- `TOKEN`=
- `CHAT_ID`=
- `MAX_DATE`=23-12-2023
- COOKIE="_vtv_session=2KV1gYxH2g8jj7SP9iRx43qapNil9XwtuJ0gfoeupWUlQfhjADYvtP7WFeHhOnc4vrIdqZwNKGjldes%2Bxeoq4FLkPOl8ceQaLSqzo%2BCbFHmtsIo8POPzLtIpMsKOE8crSn%2FMk0ZCJrp5RW0J9XjRey53%2FzUq%2BR%2FQaK03EcWZ%2FahY0Je%2B9dWXchbYXHRra8h3lrsAIoVjC2tY%2F48iomGlnMGWJKs27dj3MGmljs08t3wbMe%2BZvhjk9DOxgTdbne3nlLIfNA8H8q17GQ7mR2uysdsB4vS7Ev8gQXew1Z3lauew6cz076fbN0oPZI8%3D--L2drFEgJ1MY5muMa--4fLJkMluk8hnwjQxmLzQeA%3D%3D"
- `SLEEP_TIME_IN_SEC`=60
- `PATENTE`=
- `SEND_TO_BOT`=TRUE

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```