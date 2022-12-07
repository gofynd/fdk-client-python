"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class StoreEwaybill(BaseSchema):
    # Orders swagger.json

    
    enabled = fields.Boolean(required=False)
    

