"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ShipmentHandOverCustomerContact(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    

