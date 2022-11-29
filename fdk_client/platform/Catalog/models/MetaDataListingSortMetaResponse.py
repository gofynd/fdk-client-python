"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MetaDataListingSortMetaResponse(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
