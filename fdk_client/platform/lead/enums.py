"""Lead Platform Enum."""

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


class PriorityEnum(Enum):
    
    HIGH = "high"
    
    LOW = "low"
    
    MEDIUM = "medium"
    
    URGENT = "urgent"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PriorityEnum type")


class HistoryTypeEnum(Enum):
    
    RATING = "rating"
    
    LOG = "log"
    
    COMMENT = "comment"
    
    DIFF = "diff"
    
    THREAD = "thread"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid HistoryTypeEnum type")


class TicketSourceEnum(Enum):
    
    PLATFORM_PANEL = "platform_panel"
    
    SALES_CHANNEL = "sales_channel"
    
    PARTNER_PANEL = "partner_panel"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TicketSourceEnum type")

