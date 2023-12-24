from typing import List, Optional
import httpx
from fastapi import Depends

from configs.Environment import get_environment_variables
from configs.HTTPClient import get_http_connection

class SystemInfoRepository:
    client : httpx.AsyncClient()
    def __init__(self, client : httpx.AsyncClient() = Depends(get_http_connection)) -> None:
        self.client = client
    
    

