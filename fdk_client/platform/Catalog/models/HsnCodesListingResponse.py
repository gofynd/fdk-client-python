"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PageResponse import PageResponse



from .HsnCodesObject import HsnCodesObject



class HsnCodesListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(HsnCodesObject, required=False), required=False)
    
