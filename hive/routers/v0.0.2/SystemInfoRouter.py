from fastapi import APIRouter, Depends, status
from schemas.SystemInfo import SystemInfoSchema
from services.SystemInfoService import SystemInfoService

SystemInfoRouter = APIRouter(prefix="/v002/system", response_model=SystemInfoSchema)

@SystemInfoRouter.get("/version", response_model=SystemInfoSchema, status_code=status.HTTP_200_OK)
def get_system_current_version(systemInfoService: SystemInfoService = Depends()):
    pass

