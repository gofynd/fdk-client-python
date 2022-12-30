"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ApplicationItemSEO(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Raw(required=False)
    
    description = fields.Raw(required=False)
    

