"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DeploymentStoreSelectionFeature(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
