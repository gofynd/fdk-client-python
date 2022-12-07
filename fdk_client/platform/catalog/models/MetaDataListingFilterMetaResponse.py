"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class MetaDataListingFilterMetaResponse(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    units = fields.List(fields.Dict(required=False), required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    