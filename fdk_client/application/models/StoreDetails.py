"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StoreTiming import StoreTiming

from .StoreAddressSerializer import StoreAddressSerializer

from .SellerPhoneNumber import SellerPhoneNumber

from .StoreDepartments import StoreDepartments

from .StoreManagerSerializer import StoreManagerSerializer





from .CompanyStore import CompanyStore


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    

