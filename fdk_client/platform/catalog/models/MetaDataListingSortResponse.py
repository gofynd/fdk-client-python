"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaDataListingSortMetaResponse import MetaDataListingSortMetaResponse



class MetaDataListingSortResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingSortMetaResponse, required=False), required=False)
    
