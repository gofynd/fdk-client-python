"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreManagerSerializer import StoreManagerSerializer





from .StoreAddressSerializer import StoreAddressSerializer



from .StoreTiming import StoreTiming

from .StoreDepartments import StoreDepartments

from .CompanyStore import CompanyStore

from .SellerPhoneNumber import SellerPhoneNumber


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
