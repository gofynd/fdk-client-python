"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SendOtpEmailCommsProvider(BaseSchema):
    # Communication swagger.json

    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

