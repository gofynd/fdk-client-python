"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .SellerPhoneNumber import SellerPhoneNumber

from .LocationDayWiseSerializer import LocationDayWiseSerializer







from .Document import Document

from .GetAddressSerializer import GetAddressSerializer

from .Storeholiday1 import Storeholiday1



from .LocationManagerSerializer import LocationManagerSerializer










class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    instance_code = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    program_type = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    company = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    addverb_reference_code = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    holiday = fields.List(fields.Nested(Storeholiday1, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

