"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Results import Results



class PlatformShipmentTrack(BaseSchema):
    #  swagger.json

    
    results = fields.Nested(Results, required=False)
    
