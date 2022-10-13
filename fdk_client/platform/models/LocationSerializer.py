"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SellerPhoneNumber import SellerPhoneNumber



from .GetAddressSerializer import GetAddressSerializer

from .Document import Document

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .LocationManagerSerializer import LocationManagerSerializer



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer













from .LocationDayWiseSerializer import LocationDayWiseSerializer


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    store_type = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    code = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    

