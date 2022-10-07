"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetReportListData(BaseSchema):
    # Finance swagger.json

    
    role_name = fields.Str(required=False)
    
    listing_enabled = fields.Boolean(required=False)
    

