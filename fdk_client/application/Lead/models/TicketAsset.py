"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .TicketAssetTypeEnum import TicketAssetTypeEnum



class TicketAsset(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Nested(TicketAssetTypeEnum, required=False)
    
