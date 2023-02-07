"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CreateChannelConfig import CreateChannelConfig



class CreateChannelConfigData(BaseSchema):
    #  swagger.json

    
    config_data = fields.Nested(CreateChannelConfig, required=False)
    
