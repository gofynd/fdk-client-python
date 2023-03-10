"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ContactNumberResponse(BaseSchema):
    # Serviceability swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    

