"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer





from .Document import Document









from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .SellerPhoneNumber import SellerPhoneNumber

from .GetAddressSerializer1 import GetAddressSerializer1

from .LocationManagerSerializer import LocationManagerSerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer




class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    company = fields.Int(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer1, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    store_type = fields.Str(required=False)
    

