"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .FilerList import FilerList



class InventoryConfig(BaseSchema):
    #  swagger.json

    
    multivalues = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    
