"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class CompanyStore(BaseSchema):
    #  swagger.json

    
    company_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
