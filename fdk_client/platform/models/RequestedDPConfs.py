"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class RequestedDPConfs(BaseSchema):
    # Order swagger.json

    
    exclude_dps = fields.List(fields.Int(required=False), required=False)
    
    is_dp_assigned_manually = fields.Boolean(required=False)
    
    ewbn = fields.Raw(required=False)
    
    rdpc_id = fields.Int(required=False)
    
    awb_type = fields.Str(required=False)
    

