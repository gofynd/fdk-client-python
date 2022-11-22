"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentItemFulFillingStore(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

