"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class TransferItemsDetails(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    logo_large = fields.Str(required=False)
    
    logo_small = fields.Str(required=False)
    