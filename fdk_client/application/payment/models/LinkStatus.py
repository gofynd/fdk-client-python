"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LinkStatus(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
