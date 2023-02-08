"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TaxInfo(BaseSchema):
    #  swagger.json

    
    gstin = fields.Str(required=False)
    
    b2b_gstin_number = fields.Str(required=False)
    
