"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LinkStatus(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
