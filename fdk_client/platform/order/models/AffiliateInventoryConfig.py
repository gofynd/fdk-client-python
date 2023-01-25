"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateInventoryLogisticsConfig import AffiliateInventoryLogisticsConfig



from .AffiliateInventoryOrderConfig import AffiliateInventoryOrderConfig



from .AffiliateInventoryArticleAssignmentConfig import AffiliateInventoryArticleAssignmentConfig



from .AffiliateInventoryPaymentConfig import AffiliateInventoryPaymentConfig



from .AffiliateInventoryStoreConfig import AffiliateInventoryStoreConfig



class AffiliateInventoryConfig(BaseSchema):
    #  swagger.json

    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
