"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class TaxSlab(BaseSchema):
    #  swagger.json

    
    rate = fields.Float(required=False)
    
    cess = fields.Float(required=False)
    
    effective_date = fields.Str(required=False)
    
    threshold = fields.Float(required=False)
    
