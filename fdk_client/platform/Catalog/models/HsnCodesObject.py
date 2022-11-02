"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class HsnCodesObject(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    hs2_code = fields.Str(required=False)
    
    tax2 = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    threshold2 = fields.Float(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    tax1 = fields.Float(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    
    threshold1 = fields.Float(required=False)
    
    company_id = fields.Int(required=False)
    