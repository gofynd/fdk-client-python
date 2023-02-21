"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ProductsReasonsData(BaseSchema):
    #  swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason_text = fields.Str(required=False)
    
