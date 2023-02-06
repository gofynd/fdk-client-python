"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .NotAvailable import NotAvailable



from .Sellable import Sellable



from .OrderCommitted import OrderCommitted



from .Damaged import Damaged



class Quantities(BaseSchema):
    #  swagger.json

    
    not_available = fields.Nested(NotAvailable, required=False)
    
    sellable = fields.Nested(Sellable, required=False)
    
    order_committed = fields.Nested(OrderCommitted, required=False)
    
    damaged = fields.Nested(Damaged, required=False)
    
