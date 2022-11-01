"""Configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema






class Locations(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
