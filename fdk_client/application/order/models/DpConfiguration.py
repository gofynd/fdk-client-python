"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class DpConfiguration(BaseSchema):
    #  swagger.json

    
    shipping_by = fields.Str(required=False)
    
