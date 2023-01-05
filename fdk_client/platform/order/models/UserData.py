"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderUser import OrderUser



from .OrderUser import OrderUser



class UserData(BaseSchema):
    #  swagger.json

    
    billing_user = fields.Nested(OrderUser, required=False)
    
    shipping_user = fields.Nested(OrderUser, required=False)
    
