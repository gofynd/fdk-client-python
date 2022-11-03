"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class HistoryDict(BaseSchema):
    # OrderManage swagger.json

    
    type = fields.Str(required=False)
    
    l3_detail = fields.Str(required=False)
    
    l2_detail = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    l1_detail = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    createdat = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    ticket_url = fields.Str(required=False)
    

