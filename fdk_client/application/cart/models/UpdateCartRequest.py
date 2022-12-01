"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UpdateProductCart import UpdateProductCart





class UpdateCartRequest(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    
