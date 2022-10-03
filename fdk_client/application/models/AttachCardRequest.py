"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class AttachCardRequest(BaseSchema):
    # Payment swagger.json

    
    nickname = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False)
    
    card_id = fields.Str(required=False)
    
    name_on_card = fields.Str(required=False)
    

