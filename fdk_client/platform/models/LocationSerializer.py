"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .Storeholiday1 import Storeholiday1



from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .Document import Document

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .GetAddressSerializer import GetAddressSerializer

from .LocationManagerSerializer import LocationManagerSerializer











from .SellerPhoneNumber import SellerPhoneNumber


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    fulfilment_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    holiday = fields.List(fields.Nested(Storeholiday1, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    

