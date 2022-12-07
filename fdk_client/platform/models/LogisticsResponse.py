"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Dp import Dp




class LogisticsResponse(BaseSchema):
    # Serviceability swagger.json

    
    dp = fields.Nested(Dp, required=False)
    
    override = fields.Boolean(required=False)
    

