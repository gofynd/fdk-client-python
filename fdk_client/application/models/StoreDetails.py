"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyStore import CompanyStore

from .StoreTiming import StoreTiming



from .StoreDepartments import StoreDepartments





from .SellerPhoneNumber import SellerPhoneNumber

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreManagerSerializer import StoreManagerSerializer


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    company = fields.Nested(CompanyStore, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

