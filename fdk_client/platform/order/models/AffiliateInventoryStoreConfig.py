"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AffiliateInventoryStoreConfig(BaseSchema):
    #  swagger.json

    
    store = fields.Dict(required=False)
    
