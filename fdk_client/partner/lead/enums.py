"""Lead Partner Enum."""

from enum import Enum


class TicketAssetTypeEnum(Enum):
    
    IMAGE = "image"
    
    VIDEO = "video"
    
    FILE = "file"
    
    YOUTUBE = "youtube"
    
    PRODUCT = "product"
    
    COLLECTION = "collection"
    
    BRAND = "brand"
    
    SHIPMENT = "shipment"
    
    ORDER = "order"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TicketAssetTypeEnum type")

