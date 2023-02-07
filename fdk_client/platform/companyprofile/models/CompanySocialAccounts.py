"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CompanySocialAccounts(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
