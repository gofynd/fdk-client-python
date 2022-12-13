"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class GetBulkStatusRequest(BaseSchema):
    # DocumentEngine swagger.json

    
    batch_id = fields.Str(required=False)
    

