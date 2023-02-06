"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreateChannelConfig import CreateChannelConfig


class CreateChannelConfigData(BaseSchema):
    # OrderManage swagger.json

    
    config_data = fields.Nested(CreateChannelConfig, required=False)
    

