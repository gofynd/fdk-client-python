"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventorySellerResponse import InventorySellerResponse



from .Page import Page



class InventorySellerIdentifierResponsePaginated(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(InventorySellerResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
