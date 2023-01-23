"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


























class HsnUpsert(BaseSchema):
    #  swagger.json

    
    threshold2 = fields.Float(required=False)
    
    tax2 = fields.Float(required=False)
    
    company_id = fields.Int(required=False)
    
    tax1 = fields.Float(required=False)
    
    uid = fields.Int(required=False)
    
    tax_on_mrp = fields.Boolean(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    threshold1 = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    hs2_code = fields.Str(required=False)
    
