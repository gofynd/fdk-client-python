"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PageResponse import PageResponse



from .HSNDataInsertV2 import HSNDataInsertV2



class HsnCodesListingResponseSchemaV2(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(HSNDataInsertV2, required=False), required=False)
    
