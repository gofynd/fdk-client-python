"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .StoreMeta import StoreMeta







































from .StoreAddress import StoreAddress




















class Store1(BaseSchema):
    # Order swagger.json

    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    alohomora_user_id = fields.Int(required=False)
    
    meta = fields.Nested(StoreMeta, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    packaging_material_count = fields.Int(required=False)
    
    mall_area = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    login_username = fields.Str(required=False)
    
    mall_name = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    s_id = fields.Str(required=False)
    
    store_active_from = fields.Str(required=False)
    
    vat_no = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    phone = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    store_address_json = fields.Nested(StoreAddress, required=False)
    
    address2 = fields.Str(required=False)
    
    parent_store_id = fields.Int(required=False)
    
    longitude = fields.Float(required=False)
    
    location_type = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    brand_id = fields.Raw(required=False)
    
    is_enabled_for_recon = fields.Boolean(required=False)
    

