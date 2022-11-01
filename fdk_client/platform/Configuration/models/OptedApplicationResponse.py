"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .OptedCompany import OptedCompany



from .OptedInventory import OptedInventory



from .OptOutInventory import OptOutInventory



class OptedApplicationResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    company = fields.Nested(OptedCompany, required=False)
    
    opted_inventory = fields.Nested(OptedInventory, required=False)
    
    opt_out_inventory = fields.Nested(OptOutInventory, required=False)
    
