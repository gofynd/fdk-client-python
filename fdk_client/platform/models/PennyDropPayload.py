"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PennyDropPayload(BaseSchema):
    # Payment swagger.json

    
    enabled = fields.Boolean(required=False)
    
    service_provider = fields.Str(required=False)
    

