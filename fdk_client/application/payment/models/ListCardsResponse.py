"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .Card import Card



class ListCardsResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
