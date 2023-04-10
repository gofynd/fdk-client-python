"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EdcDevice import EdcDevice

from .Page import Page




class EdcDeviceListResponse(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(EdcDevice, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    

