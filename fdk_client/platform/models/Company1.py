"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





































from .CompanyMeta import CompanyMeta






class Company1(BaseSchema):
    # Order swagger.json

    
    pan_no = fields.Str(required=False)
    
    agreement_start_date = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    exchange_allowed = fields.Boolean(required=False)
    
    payment_type = fields.Str(required=False)
    
    cst = fields.Str(required=False)
    
    commission = fields.Float(required=False)
    
    created_on = fields.Int(required=False)
    
    payment_procesing_charge = fields.Float(required=False)
    
    fynd_a_fit_available = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    
    modified_on = fields.Int(required=False)
    
    company_name = fields.Str(required=False)
    
    exchange_within_days = fields.Int(required=False)
    
    tan_no = fields.Str(required=False)
    
    c_id = fields.Int(required=False)
    
    vat_no = fields.Str(required=False)
    
    gst_number = fields.Str(required=False)
    
    meta = fields.Nested(CompanyMeta, required=False)
    
    business_type = fields.Str(required=False)
    
    return_within_days = fields.Int(required=False)
    

