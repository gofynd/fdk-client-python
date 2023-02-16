"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DeploymentMeta import DeploymentMeta



class OrderingStoreConfig(BaseSchema):
    #  swagger.json

    
    deployment_meta = fields.Nested(DeploymentMeta, required=False)
    
