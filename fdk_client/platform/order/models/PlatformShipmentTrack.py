"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PlatformTrack import PlatformTrack





class PlatformShipmentTrack(BaseSchema):
    #  swagger.json

    
    results = fields.List(fields.Nested(PlatformTrack, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
