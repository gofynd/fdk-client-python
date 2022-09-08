"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Documents1 import Documents1





from .CompanyAddress import CompanyAddress






class CompanyMeta(BaseSchema):
    # Order swagger.json

    
    business_info = fields.Str(required=False)
    
    documents = fields.Nested(Documents1, required=False)
    
    business_details = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.List(fields.Nested(CompanyAddress, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_details = fields.Dict(required=False)
    

