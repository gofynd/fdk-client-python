"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig

from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig

from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig

from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig

from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig


class AffiliateInventoryConfig(BaseSchema):
    # OrderManage swagger.json

    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    

