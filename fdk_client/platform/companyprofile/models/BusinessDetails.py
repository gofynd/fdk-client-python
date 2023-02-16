"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Website import Website



class BusinessDetails(BaseSchema):
    #  swagger.json

    
    website = fields.Nested(Website, required=False)
    
