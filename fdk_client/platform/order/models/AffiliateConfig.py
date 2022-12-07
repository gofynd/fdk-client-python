"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateInventoryConfig import AffiliateInventoryConfig



from .AffiliateAppConfig import AffiliateAppConfig



class AffiliateConfig(BaseSchema):
    #  swagger.json

    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    
    app = fields.Nested(AffiliateAppConfig, required=False)
    
