"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StatuesResponse import StatuesResponse


class StatusUpdateInternalResponse(BaseSchema):
    # OrderManage swagger.json

    
    statuses = fields.List(fields.Nested(StatuesResponse, required=False), required=False)
    

