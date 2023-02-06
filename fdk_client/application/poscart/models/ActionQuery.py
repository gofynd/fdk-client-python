"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ActionQuery(BaseSchema):
    #  swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    
