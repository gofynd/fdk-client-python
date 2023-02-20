"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class BuyerDetails(BaseSchema):
    #  swagger.json

    
    pincode = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    ajio_site_id = fields.Str(required=False)
    
