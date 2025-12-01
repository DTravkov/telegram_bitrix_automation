import os
import pytz
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv(".venv/envar.env")
CITY_TZ_NAME = os.getenv("CITY_TZ_NAME")


def current_time_minus_2h():
    tz = pytz.timezone(CITY_TZ_NAME)
    time = (datetime.now(tz=tz) - timedelta(hours=2)).isoformat(timespec='seconds')

    return time



def current_time_plus_2h():
    tz = pytz.timezone(CITY_TZ_NAME)
    time = (datetime.now(tz=tz) + timedelta(hours=2)).isoformat(timespec='seconds')

    return time
