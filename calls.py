
import os
import httpx
from typing import List
from dotenv import load_dotenv

from utils import current_time_minus_2h, current_time_plus_2h
from classes import LeadMessage

load_dotenv(".venv/envar.env")

BITRIX_URL = os.getenv("BITRIX_URL")


async def fetch_leads_list(filtered_2h=False) -> List[LeadMessage]:

    params = {
        "filter": {}, 
        "select" : ["*","UF_*"], 
        "start": -1  
    }

    if filtered_2h:
        params['filter']["<DATE_CREATE"] = current_time_minus_2h()
        print("Time filter is active, only leads registered > 2hrs ago are fetched. To remove this filter, change GET_ONLY_LEADS_FROM_2HRS_AGO in main.py to False")
    else:
        print("Time filter is inactive, all the leads will be fetched. To add this filter, change GET_ONLY_LEADS_FROM_2HRS_AGO in main.py to True")
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:

            response = await client.post(BITRIX_URL + '/crm.lead.list' ,json=params)
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


async def fetch_lead_contact_by_id(contact_id):

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            params = {
                "id" : contact_id
                }
            response = await client.post(BITRIX_URL + '/crm.contact.get',json=params)
            response.raise_for_status()

            return response.json()['result']
        
        except httpx.TimeoutException:
            print("POST request timed out")
        except httpx.HTTPStatusError as e:
            print(f"POST HTTP error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
        except Exception as e:
            print(f"Unexpected POST error: {e}")
        return None
    
async def lead_add_comment_by_id(lead_id, comment_text):

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            params = {
            "fields": {
                "ENTITY_ID": lead_id,
                "ENTITY_TYPE": "lead",
                "COMMENT": f"{comment_text}"
                }
            }
            response = await client.post(BITRIX_URL + '/crm.timeline.comment.add',json=params)
            response.raise_for_status()

            print(f"Comment  {comment_text} was added successfully!")
        
        except httpx.TimeoutException:
            print("POST request timed out")
        except httpx.HTTPStatusError as e:
            print(f"POST HTTP error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
        except Exception as e:
            print(f"Unexpected POST error: {e}")
        return None


async def lead_add_task_by_id(lead_id, task_text):

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            
            deadline = current_time_plus_2h()

            params = {
                "fields": {
                    "TITLE": f"Follow-up for Lead by id {lead_id}",
                    "RESPONSIBLE_ID": 1,
                    "DEADLINE": deadline,
                    "UF_CRM_TASK": [ f"L_{lead_id}" ] 
                }
            }

            response = await client.post(BITRIX_URL + '/tasks.task.add', json=params)
            response.raise_for_status()
            print("Task was added successfully")
        
        except httpx.TimeoutException:
            print("POST request timed out")
        except httpx.HTTPStatusError as e:
            print(f"POST HTTP error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
        except Exception as e:
            print(f"Unexpected POST error: {e}")
        return None
    