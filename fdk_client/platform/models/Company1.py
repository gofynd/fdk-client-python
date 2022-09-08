"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









































from .CompanyMeta import CompanyMeta


class Company1(BaseSchema):
    # Order swagger.json

    
    company_type = fields.Str(required=False)
    
    payment_type = fields.Str(required=False)
    
    exchange_within_days = fields.Int(required=False)
    
    modified_on = fields.Int(required=False)
    
    fynd_a_fit_available = fields.Boolean(required=False)
    
    cst = fields.Str(required=False)
    
    created_on = fields.Int(required=False)
    
    c_id = fields.Int(required=False)
    
    payment_procesing_charge = fields.Float(required=False)
    
    business_type = fields.Str(required=False)
    
    gst_number = fields.Str(required=False)
    
    return_allowed = fields.Boolean(required=False)
    
    tan_no = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    commission = fields.Float(required=False)
    
    company_name = fields.Str(required=False)
    
    exchange_allowed = fields.Boolean(required=False)
    
    agreement_start_date = fields.Int(required=False)
    
    return_within_days = fields.Int(required=False)
    
    vat_no = fields.Str(required=False)
    
    meta = fields.Nested(CompanyMeta, required=False)
    

