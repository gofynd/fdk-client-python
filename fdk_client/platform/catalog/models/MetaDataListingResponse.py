"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaDataListingSortResponse import MetaDataListingSortResponse



from .MetaDataListingFilterResponse import MetaDataListingFilterResponse



class MetaDataListingResponse(BaseSchema):
    #  swagger.json

    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    
