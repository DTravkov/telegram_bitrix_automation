
import os
import httpx
from typing import List
from dotenv import load_dotenv

from utils import current_time_minus_2h
from classes import LeadMessage

load_dotenv(".venv/envar.env")

BITRIX_URL_LEADS = os.getenv("BITRIX_URL_LEADS")


async def fetch_leads_list(filtered_2h=False) -> List[LeadMessage]:

    params = {
        "filter": {}, 
        "select" : ["*","UF_*"], 
        "start": -1  
    }

    if filtered_2h:
        params['filter']["<DATE_CREATED"] = current_time_minus_2h()

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:

            response = await client.post(BITRIX_URL_LEADS + '/crm.lead.list' ,json=params)
            response.raise_for_status()

            return [LeadMessage(x) for x in response.json()['result']]
        
        except httpx.TimeoutException:
            print("POST request timed out")
        except httpx.HTTPStatusError as e:
            print(f"POST HTTP error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
        except Exception as e:
            print(f"Unexpected POST error: {e}")
        return None
