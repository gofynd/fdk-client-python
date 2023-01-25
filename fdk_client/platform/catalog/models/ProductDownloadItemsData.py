"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductDownloadItemsData(BaseSchema):
    #  swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    templates = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
