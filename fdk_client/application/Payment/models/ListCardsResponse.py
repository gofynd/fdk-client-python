"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Card import Card







class ListCardsResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
