"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig

from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig

from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig

from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig

from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig


class AffiliateInventoryConfig(BaseSchema):
    # OrderManage swagger.json

    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    

