"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class TransferItemsDetails(BaseSchema):

    
    display_name = fields.Boolean(required=False)
    
    logo_small = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo_large = fields.Str(required=False)
    

