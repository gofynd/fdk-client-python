"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig



from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig



from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig



from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig



from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig



class AffiliateInventoryConfig(BaseSchema):
    #  swagger.json

    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
