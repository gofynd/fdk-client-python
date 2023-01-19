"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class StoreEinvoice(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    user = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
