"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class StorePriority(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    storetype_order = fields.List(fields.Raw(required=False), required=False)
    
