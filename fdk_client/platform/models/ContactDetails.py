"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PhoneDetails import PhoneDetails




class ContactDetails(BaseSchema):
    # Order swagger.json

    
    phone = fields.List(fields.Nested(PhoneDetails, required=False), required=False)
    
    emails = fields.List(fields.Str(required=False), required=False)
    

