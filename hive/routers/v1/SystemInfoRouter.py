from fastapi import APIRouter, Depends, status
from schemas.SystemInfo import SystemInfoSchema
from services.SystemInfoService import SystemInfoService
from configs.Environment import get_environment_variables
from metadata.Tags import Tags
env = get_environment_variables()
SystemInfoRouter = APIRouter(prefix=f"/{env.API_VERSION}/system", tags=[Tags[0]["name"]])

@SystemInfoRouter.get("/version", response_model=SystemInfoSchema, status_code=status.HTTP_200_OK)
def get_system_current_version(systemInfoService: SystemInfoService = Depends()):
    return systemInfoService.get_system_version()

