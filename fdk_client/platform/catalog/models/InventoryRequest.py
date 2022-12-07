"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InvSize import InvSize



from .ItemQuery import ItemQuery





class InventoryRequest(BaseSchema):
    #  swagger.json

    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    item = fields.Nested(ItemQuery, required=False)
    
    company_id = fields.Int(required=False)
    
