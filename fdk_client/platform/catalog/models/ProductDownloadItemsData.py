"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductDownloadItemsData(BaseSchema):
    #  swagger.json

    
    templates = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    