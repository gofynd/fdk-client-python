"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class UpdateAddressResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    