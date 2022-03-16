"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .GetAddressSerializer1 import GetAddressSerializer1



from .Document import Document



from .SellerPhoneNumber import SellerPhoneNumber

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .LocationManagerSerializer import LocationManagerSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer








class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    

