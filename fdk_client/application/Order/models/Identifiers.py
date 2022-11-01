"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Identifiers(BaseSchema):
    #  swagger.json

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    
