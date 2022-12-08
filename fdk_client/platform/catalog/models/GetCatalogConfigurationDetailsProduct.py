"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class GetCatalogConfigurationDetailsProduct(BaseSchema):
    #  swagger.json

    
    compare = fields.Dict(required=False)
    
    detail = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    
    similar = fields.Dict(required=False)
    
