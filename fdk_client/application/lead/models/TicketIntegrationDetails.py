"""lead Application Enum."""

from enum import Enum

class TicketIntegrationDetails(Enum):
    
    DEFAULT = "default"
    
    FRESHDESK = "freshdesk"
    
    KAPTURE = "kapture"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TicketIntegrationDetails type")

