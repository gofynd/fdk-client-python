"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class DomainAdd(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    txt_records = fields.List(fields.Str(required=False), required=False)
    
