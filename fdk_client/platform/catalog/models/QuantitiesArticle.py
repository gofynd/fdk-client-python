"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Quantity import Quantity



from .Quantity import Quantity



from .Quantity import Quantity



from .Quantity import Quantity



class QuantitiesArticle(BaseSchema):
    #  swagger.json

    
    sellable = fields.Nested(Quantity, required=False)
    
    not_available = fields.Nested(Quantity, required=False)
    
    order_committed = fields.Nested(Quantity, required=False)
    
    damaged = fields.Nested(Quantity, required=False)
    
