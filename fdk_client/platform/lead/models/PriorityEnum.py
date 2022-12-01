"""lead Platform Enum."""

from enum import Enum

class PriorityEnum(Enum):
    
    LOW = "low"
    
    MEDIUM = "medium"
    
    HIGH = "high"
    
    URGENT = "urgent"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PriorityEnum type")

