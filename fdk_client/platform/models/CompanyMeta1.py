"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CompanyMeta1(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    

