"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PageResponse import PageResponse



from .ItemResponse import ItemResponse



class GetStoresViewResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    
