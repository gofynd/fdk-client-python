"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CountryMetaResponse(BaseSchema):
    #  swagger.json

    
    isd_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
