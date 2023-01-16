"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ActionQuery import ActionQuery







class ProductAction(BaseSchema):
    #  swagger.json

    
    query = fields.Nested(ActionQuery, required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    