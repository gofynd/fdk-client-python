"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class HSNData(BaseSchema):
    #  swagger.json

    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    
