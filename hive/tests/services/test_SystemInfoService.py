from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.SystemInfoRepo import SystemInfoRepository

from services.SystemInfoService import SystemInfoService

class TestSystemInfoService(TestCase):
    systemInfoRepo : SystemInfoRepository
    systemInfoService: SystemInfoService
    
    def setUp(self):
        super().setUp()
        self.systemInfoRepo = create_autospec(
            SystemInfoRepository
        )
        self.systemInfoService = SystemInfoService(
            self.systemInfoRepo
        )
    
    def test_get(self):
        self.systemInfoService.get_system_version()

        self.systemInfoRepo.get_system_version.assert_called_once()