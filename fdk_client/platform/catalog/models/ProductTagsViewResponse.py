"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .NestedTags import NestedTags



class ProductTagsViewResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(NestedTags, required=False)
    
