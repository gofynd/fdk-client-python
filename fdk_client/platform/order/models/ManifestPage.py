"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ManifestPage(BaseSchema):
    #  swagger.json

    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    current = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
