"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig

from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig

from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig

from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig

from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig


class AffiliateInventoryConfig(BaseSchema):
    # Order swagger.json

    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    

