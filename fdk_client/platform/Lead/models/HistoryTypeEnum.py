"""Lead Platform Enum."""

from enum import Enum

class HistoryTypeEnum(Enum):
    
    RATING = "rating"
    
    LOG = "log"
    
    COMMENT = "comment"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid HistoryTypeEnum type")

