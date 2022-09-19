"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetAddressSerializer import GetAddressSerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .Document import Document



from .LocationDayWiseSerializer import LocationDayWiseSerializer







from .SellerPhoneNumber import SellerPhoneNumber

from .LocationManagerSerializer import LocationManagerSerializer













from .InvoiceDetailsSerializer import InvoiceDetailsSerializer


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    

