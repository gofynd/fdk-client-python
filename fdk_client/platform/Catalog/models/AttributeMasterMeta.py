"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AttributeMasterMandatoryDetails import AttributeMasterMandatoryDetails





class AttributeMasterMeta(BaseSchema):
    #  swagger.json

    
    mandatory_details = fields.Nested(AttributeMasterMandatoryDetails, required=False)
    
    enriched = fields.Boolean(required=False)
    
