"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class HsnUpsert(BaseSchema):
    #  swagger.json

    
    company_id = fields.Int(required=False)
    
    hs2_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    threshold1 = fields.Float(required=False)
    
    tax1 = fields.Float(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    tax2 = fields.Float(required=False)
    
    threshold2 = fields.Float(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    hsn_code = fields.Str(required=False)
    
