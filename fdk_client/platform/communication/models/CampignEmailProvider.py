"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CampignEmailProvider(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    from_email = fields.Str(required=False)
    
