"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .QuantityBase import QuantityBase



from .QuantityBase import QuantityBase



from .QuantityBase import QuantityBase



from .QuantityBase import QuantityBase



class Quantities(BaseSchema):
    #  swagger.json

    
    sellable = fields.Nested(QuantityBase, required=False)
    
    order_committed = fields.Nested(QuantityBase, required=False)
    
    damaged = fields.Nested(QuantityBase, required=False)
    
    not_available = fields.Nested(QuantityBase, required=False)
    
