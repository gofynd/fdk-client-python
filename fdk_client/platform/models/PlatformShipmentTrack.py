"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PlatformTrack import PlatformTrack




class PlatformShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(PlatformTrack, required=False), required=False)
    
    meta = fields.Dict(required=False)
    

