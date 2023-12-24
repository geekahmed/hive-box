from fastapi import Depends
from schemas.SystemInfo import SystemInfoSchema
from repositories.SystemInfoRepo import SystemInfoRepository
from models.SystemInfo import SystemInfo
class SystemInfoService:

    systemInfoRepo: SystemInfoRepository

    def __init__(self, systemInfoRepo: SystemInfoRepository = Depends()) -> None:
        self.systemInfoRepo = systemInfoRepo
    
    def get_system_version(self) -> SystemInfo:
        return self.systemInfoRepo.get_system_version()
    
    

