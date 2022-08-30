"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CompanyAddress import CompanyAddress

from .Documents1 import Documents1








class CompanyMeta(BaseSchema):
    # Order swagger.json

    
    contact_details = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    address = fields.List(fields.Nested(CompanyAddress, required=False), required=False)
    
    documents = fields.Nested(Documents1, required=False)
    
    business_info = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    business_details = fields.Dict(required=False)
    

