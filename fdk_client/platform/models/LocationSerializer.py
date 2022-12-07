"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .LocationDayWiseSerializer import LocationDayWiseSerializer









from .LocationManagerSerializer import LocationManagerSerializer

from .GetAddressSerializer import GetAddressSerializer

from .SellerPhoneNumber import SellerPhoneNumber





from .Document import Document

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer








class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    company = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    display_name = fields.Str(required=False)
    

