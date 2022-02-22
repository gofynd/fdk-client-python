"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class DataItems(BaseSchema):
    # Communication swagger.json

    
    to = fields.Str(required=False)
    
    cc = fields.Str(required=False)
    
    bcc = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    ref_user = fields.Str(required=False)
    
    ref_application = fields.Str(required=False)
    

