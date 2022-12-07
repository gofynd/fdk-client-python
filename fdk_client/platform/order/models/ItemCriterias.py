"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ItemCriterias(BaseSchema):
    #  swagger.json

    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
