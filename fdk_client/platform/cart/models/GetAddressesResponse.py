"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Address import Address



class GetAddressesResponse(BaseSchema):
    #  swagger.json

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    
