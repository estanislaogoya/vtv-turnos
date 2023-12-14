import logging
import os
from dotenv import load_dotenv
import requests
import datetime
import time
import json

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

plantas = {
    "24": "VICENTE LOPEZ",
    "71": "PILAR",
    "25": "SAN MARTIN",
    "74": "TIGRE",
    "26": "ZARATE",
    "8": "ITUZAINGO",
    "83": "BELEN DE ESCOBAR",
    "27": "CAPITAN SARMIENTO",
    "48": "CARMEN DE ARECO",
    "142": "SAN ANTONIO DE ARECO"
}


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": os.environ['COOKIE'],
    "If-None-Match": "W/fac07fc2873f5367169398f226c43a73",
    "Referer": "https://vtvpba.minfra.gba.gob.ar/SolicitudTurno",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def _generate_url(planta):
 return f"https://vtvpba.minfra.gba.gob.ar/turnos_por_fechas.json?planta_id={planta}&dominio={os.environ['PATENTE']}"


def _send_to_tg(msg):
    TOKEN = os.environ['TOKEN']
    CHAT_ID = os.environ['CHAT_ID']
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    return requests.get(url) # this sends the message

def _check_if_results_ok(json_str, planta_value):

    exito = False

    date_format = '%d-%m-%Y'

    fechas = []

    try:
        if json_str:
            if json_str['results']:
                for i in range(0,len(json_str['results'])-1):

                    fechas.append(datetime.datetime.strptime(json_str['results'][i]['fecha'], date_format))
                    #TOP 3 Fechas
                    if i == 2:
                        break

                max_date = datetime.datetime.strptime(os.environ['MAX_DATE'], date_format )

                for fecha in fechas:
                    delta = fecha - max_date

                    delta_now = fecha - datetime.datetime.now()
                    
                    if delta.days <= 0:
                        txt = f"TURNO ENCONTRADO! Planta: {planta_value}; En {delta_now.days} dias ({fecha})"
                        if os.environ['SEND_TO_BOT'].lower() == 'true': 
                            _send_to_tg(txt)
                        else:
                            logger.info(txt)

                        exito = True
            else:
                logger.info(f"No results: {json_str}")
        else:
            logger.info(f"json_str had problems {json_str}")
    except Exception as e:
        logger.error(f"Exception happened: {e}")


    return exito

def _sleep():
    logger.info(f"sleeping: {int(os.environ['SLEEP_TIME_IN_SEC'])} seconds")
    time.sleep(int(os.environ['SLEEP_TIME_IN_SEC']))

def run():
    load_dotenv()
    exito = False
    errors = []
    try:
        while exito == False:
            for planta_key, planta_value in plantas.items():
                logger.info(f"processing planta: {planta_value}")
                rsp = requests.get(_generate_url(planta_key), headers=headers)
                logger.debug(f"Response content: {rsp.text}")

                if not rsp.content:
                    logger.warning(f"Empty response for planta: {planta_value}")
                    continue  # Skip processing this planta if the response is empty

                if rsp.status_code != 200:
                    logger.info(f"Response error: {rsp.text}")
                else:
                    try:
                        rsp_json = rsp.json()
                        exito = _check_if_results_ok(rsp_json, planta_value)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error decoding JSON response for planta {planta_value}: {e}")
                        continue  # Skip processing this planta if there's a JSON decoding error
            _sleep()

    except Exception as e:
        errors.append(e)
        logger.error(f"Exception happened: {e}")
        if os.environ['SEND_TO_BOT'].lower() == 'true': 
            _send_to_tg(f"Exception happened: {e}")
    return errors

if __name__ == "__main__":
    run()