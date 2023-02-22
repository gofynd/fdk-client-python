"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class GetCatalogConfigurationDetailsProduct(BaseSchema):
    #  swagger.json

    
    similar = fields.Dict(required=False)
    
    compare = fields.Dict(required=False)
    
    detail = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    
