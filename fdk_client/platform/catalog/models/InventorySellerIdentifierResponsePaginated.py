"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .InventorySellerResponse import InventorySellerResponse



class InventorySellerIdentifierResponsePaginated(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(InventorySellerResponse, required=False), required=False)
    
