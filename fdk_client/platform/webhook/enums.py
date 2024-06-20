"""Webhook Platform Enum."""

from enum import Enum


class SubscriberStatus(Enum):
    
    ACTIVE = "active"
    
    INACTIVE = "inactive"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid SubscriberStatus type")

