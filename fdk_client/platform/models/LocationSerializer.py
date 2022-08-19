"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Storeholiday1 import Storeholiday1

from .SellerPhoneNumber import SellerPhoneNumber







from .LocationManagerSerializer import LocationManagerSerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .GetAddressSerializer import GetAddressSerializer







from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .Document import Document


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    fulfilment_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    holiday = fields.List(fields.Nested(Storeholiday1, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    addverb_reference_code = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    

