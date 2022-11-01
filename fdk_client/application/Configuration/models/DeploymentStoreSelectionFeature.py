"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class DeploymentStoreSelectionFeature(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
