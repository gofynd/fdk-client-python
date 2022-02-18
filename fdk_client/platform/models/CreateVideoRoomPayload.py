"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CreateVideoRoomPayload(BaseSchema):
    # Lead swagger.json

    
    unique_name = fields.Str(required=False)
    
    notify = fields.List(fields.Dict(required=False), required=False)
    

