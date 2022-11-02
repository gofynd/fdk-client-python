"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class LocationIntegrationType(BaseSchema):
    #  swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    
