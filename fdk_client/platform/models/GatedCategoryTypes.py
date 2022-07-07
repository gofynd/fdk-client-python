"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class GatedCategoryTypes(BaseSchema):
    # Catalog swagger.json

    
    food = fields.Boolean(required=False)
    

