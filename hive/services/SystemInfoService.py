from fastapi import Depends
from schemas.SystemInfo import SystemInfoSchema
from repositories.SystemInfoRepo import SystemInfoRepository

class SystemInfoService:

    systemInfoRepo: SystemInfoRepository

    def __init__(self, systemInfoRepo: SystemInfoRepository = Depends()) -> None:
        self.systemInfoRepo = systemInfoRepo
    
    

