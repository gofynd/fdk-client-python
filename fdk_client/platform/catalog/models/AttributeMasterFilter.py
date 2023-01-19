"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class AttributeMasterFilter(BaseSchema):
    #  swagger.json

    
    priority = fields.Int(required=False)
    
    depends_on = fields.List(fields.Str(required=False), required=False)
    
    indexing = fields.Boolean(required=False)
    
