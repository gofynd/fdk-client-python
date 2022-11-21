"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StoreManagerSerializer import StoreManagerSerializer

from .SellerPhoneNumber import SellerPhoneNumber

from .StoreTiming import StoreTiming

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreDepartments import StoreDepartments

from .CompanyStore import CompanyStore






class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    

