"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CommunicationOptinDialogFeature(BaseSchema):
    #  swagger.json

    
    visibility = fields.Boolean(required=False)
    
