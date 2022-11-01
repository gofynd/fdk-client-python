"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaDataListingFilterMetaResponse import MetaDataListingFilterMetaResponse



class MetaDataListingFilterResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponse, required=False), required=False)
    
