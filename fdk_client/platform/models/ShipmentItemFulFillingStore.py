"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentItemFulFillingStore(BaseSchema):
    # Orders swagger.json

    
    code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

