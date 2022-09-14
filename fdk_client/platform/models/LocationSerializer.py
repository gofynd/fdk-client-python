"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .LocationDayWiseSerializer import LocationDayWiseSerializer

















from .GetAddressSerializer import GetAddressSerializer

from .Storeholiday1 import Storeholiday1





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .LocationManagerSerializer import LocationManagerSerializer

from .Document import Document

from .SellerPhoneNumber import SellerPhoneNumber






class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    instance_code = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    holiday = fields.List(fields.Nested(Storeholiday1, required=False), required=False)
    
    program_type = fields.Str(required=False)
    
    addverb_reference_code = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    company = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    

