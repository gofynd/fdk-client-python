"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityReasonData(BaseSchema):
    # OrderManage swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    

