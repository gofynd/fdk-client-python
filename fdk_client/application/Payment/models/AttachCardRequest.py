"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class AttachCardRequest(BaseSchema):
    #  swagger.json

    
    card_id = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    name_on_card = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False)
    
