"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateAppConfig import AffiliateAppConfig



from .AffiliateInventoryConfig import AffiliateInventoryConfig



class AffiliateConfig(BaseSchema):
    #  swagger.json

    
    app = fields.Nested(AffiliateAppConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    
