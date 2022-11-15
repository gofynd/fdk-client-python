"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .LatLong import LatLong











class Store(BaseSchema):
    #  swagger.json

    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    lat_long = fields.Nested(LatLong, required=False)
    
    uid = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
