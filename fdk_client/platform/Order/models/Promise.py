"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Timestamp import Timestamp



class Promise(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Nested(Timestamp, required=False)
    
