"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaDataListingFilterResponse import MetaDataListingFilterResponse



from .MetaDataListingSortResponse import MetaDataListingSortResponse



class MetaDataListingResponse(BaseSchema):
    #  swagger.json

    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    
