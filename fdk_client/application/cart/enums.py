"""Cart Application Enum."""

from enum import Enum


class OrderingSource(Enum):
    
    STOREFRONT = "storefront"
    
    STORE_OS_POS = "store_os_pos"
    
    KIOSK = "kiosk"
    
    SCAN_GO = "scan_go"
    
    SMART_TROLLEY = "smart_trolley"
    
    MARKETPLACE = "marketplace"
    
    SOCIAL_COMMERCE = "social_commerce"
    
    ONDC = "ondc"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid OrderingSource type")

