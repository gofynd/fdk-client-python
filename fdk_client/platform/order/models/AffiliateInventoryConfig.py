"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig



from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig



from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig



from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig



from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig



class AffiliateInventoryConfig(BaseSchema):
    #  swagger.json

    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
