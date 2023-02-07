"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ActionQuery(BaseSchema):
    #  swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    
