"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StageItem import StageItem



class OrderLanesCount(BaseSchema):
    #  swagger.json

    
    stages = fields.List(fields.Nested(StageItem, required=False), required=False)
    
