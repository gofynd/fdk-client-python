"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CompanyDetail(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
