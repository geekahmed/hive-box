from fastapi import Depends
from models.SystemInfo import SystemInfo
from configs.Environment import get_environment_variables

class SystemInfoRepository:
    
    env = get_environment_variables()
    
    def __init__(self) -> None:
        pass
    
    def get_system_version(self) -> SystemInfo:
        return SystemInfo(version=self.env.API_VERSION)
    
    

