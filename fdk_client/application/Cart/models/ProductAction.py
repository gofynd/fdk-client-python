"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ActionQuery import ActionQuery





class ProductAction(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    
