"""Payment Platform Enum."""

from enum import Enum


class StatusSchema(Enum):
    
    STARTED = "started"
    
    COMPLETED = "completed"
    
    PARTIAL_PAID = "partial_paid"
    
    FAILED = "failed"
    
    PENDING = "pending"
    
    REFUND_DONE = "refund_done"
    
    REFUND_INITIATED = "refund_initiated"
    
    PARTIAL_REFUND = "partial_refund"
    
    REFUND_FAILED = "refund_failed"
    
    REFUND_PENDING = "refund_pending"
    
    REFUND_ACKNOWLEDGE = "refund_acknowledge"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid StatusSchema type")


class DeviceTypeSchema(Enum):
    
    ANDROID = "android"
    
    IOS = "ios"
    
    DESKTOP = "desktop"
    
    IOS_POS = "ios-pos"
    
    ANDROID_POS = "android-pos"
    
    DESKTOP_PAYMENT_LINK = "desktop-payment_link"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid DeviceTypeSchema type")


class TransactionTypeSchema(Enum):
    
    FORWARD = "FORWARD"
    
    REFUND = "REFUND"
    
    AUTO_REFUND = "AUTO_REFUND"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TransactionTypeSchema type")

