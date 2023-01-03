"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TransferItemsDetails import TransferItemsDetails



class TransferModeDetails(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    
