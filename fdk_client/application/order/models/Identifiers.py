"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Identifiers(BaseSchema):
    #  swagger.json

    
    sku_code = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    
