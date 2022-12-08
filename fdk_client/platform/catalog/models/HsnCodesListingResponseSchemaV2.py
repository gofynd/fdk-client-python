"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HSNDataInsertV2 import HSNDataInsertV2



from .PageResponse import PageResponse



class HsnCodesListingResponseSchemaV2(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(HSNDataInsertV2, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    
