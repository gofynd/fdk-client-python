"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CommunicationOptinDialogFeature(BaseSchema):
    #  swagger.json

    
    visibility = fields.Boolean(required=False)
    
