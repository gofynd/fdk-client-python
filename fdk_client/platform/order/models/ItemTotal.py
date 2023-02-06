"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ItemTotal(BaseSchema):
    #  swagger.json

    
    new = fields.Int(required=False)
    
    processing = fields.Int(required=False)
    
    returns = fields.Int(required=False)
    
    all = fields.Int(required=False)
    
