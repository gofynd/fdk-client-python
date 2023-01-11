"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ItemQuery import ItemQuery



from .InvSize import InvSize





class InventoryRequest(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(ItemQuery, required=False)
    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
