"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HsnCodesObject import HsnCodesObject



from .PageResponse import PageResponse



class HsnCodesListingResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(HsnCodesObject, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    
