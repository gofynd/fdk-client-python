"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ListViewProduct(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
