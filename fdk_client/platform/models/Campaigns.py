"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Campaign import Campaign

from .Page import Page


class Campaigns(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Campaign, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

