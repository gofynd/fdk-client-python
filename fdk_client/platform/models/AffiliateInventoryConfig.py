"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig

from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig

from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig

from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig

from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig


class AffiliateInventoryConfig(BaseSchema):
    # OrderManage swagger.json

    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    

