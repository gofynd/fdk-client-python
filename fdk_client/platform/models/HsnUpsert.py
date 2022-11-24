"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class HsnUpsert(BaseSchema):
    # Catalog swagger.json

    
    tax2 = fields.Float(required=False)
    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    threshold1 = fields.Float(required=False)
    
    hs2_code = fields.Str(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    
    threshold2 = fields.Float(required=False)
    
    tax1 = fields.Float(required=False)
    

