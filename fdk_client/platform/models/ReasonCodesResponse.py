"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .ReasonCodes import ReasonCodes


class ReasonCodesResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ReasonCodes, required=False), required=False)
    

