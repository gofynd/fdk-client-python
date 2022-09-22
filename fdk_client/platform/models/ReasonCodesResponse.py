"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReasonCodes import ReasonCodes

from .Page import Page


class ReasonCodesResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(ReasonCodes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

