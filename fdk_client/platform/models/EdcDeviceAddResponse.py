"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EdcDevice import EdcDevice




class EdcDeviceAddResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EdcDevice, required=False)
    
    success = fields.Boolean(required=False)
    

