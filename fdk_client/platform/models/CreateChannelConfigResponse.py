"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CreateChannelConfigResponse(BaseSchema):
    # OrderManage swagger.json

    
    is_inserted = fields.Boolean(required=False)
    
    is_upserted = fields.Boolean(required=False)
    
    acknowledged = fields.Boolean(required=False)
    
