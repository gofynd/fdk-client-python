"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class AttachCardsResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
