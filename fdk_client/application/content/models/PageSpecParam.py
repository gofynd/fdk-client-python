"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PageSpecParam(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    