"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StoreAddressSerializer import StoreAddressSerializer



from .StoreManagerSerializer import StoreManagerSerializer

from .StoreTiming import StoreTiming

from .SellerPhoneNumber import SellerPhoneNumber

from .CompanyStore import CompanyStore

from .StoreDepartments import StoreDepartments




class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    

