"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BusinessCountryInfo(BaseSchema):
    #  swagger.json

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
