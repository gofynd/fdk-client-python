"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PlatformMobile(BaseSchema):
    #  swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    
