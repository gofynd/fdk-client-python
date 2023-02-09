"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemResponse import ItemResponse



from .ServiceabilityPageResponse import ServiceabilityPageResponse



class GetStoresViewResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    
    page = fields.Nested(ServiceabilityPageResponse, required=False)
    
