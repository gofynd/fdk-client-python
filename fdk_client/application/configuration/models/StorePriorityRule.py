"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class StorePriorityRule(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    storetype_order = fields.List(fields.Str(required=False), required=False)
    
