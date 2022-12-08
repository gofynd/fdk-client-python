"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ProductsReasonsData(BaseSchema):
    #  swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
