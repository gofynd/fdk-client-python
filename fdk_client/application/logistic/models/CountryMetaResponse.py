"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CountryMetaResponse(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    isd_code = fields.Str(required=False)
    
