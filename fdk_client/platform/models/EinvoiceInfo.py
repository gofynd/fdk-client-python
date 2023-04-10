"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EinvoiceInfo(BaseSchema):
    # Order swagger.json

    
    invoice = fields.Dict(required=False)
    
    credit_note = fields.Dict(required=False)
    

