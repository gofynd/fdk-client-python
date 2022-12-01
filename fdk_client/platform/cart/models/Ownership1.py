"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Ownership1(BaseSchema):
    #  swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    
