"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreTiming import StoreTiming



from .StoreManagerSerializer import StoreManagerSerializer

from .StoreDepartments import StoreDepartments

from .SellerPhoneNumber import SellerPhoneNumber



from .CompanyStore import CompanyStore

from .StoreAddressSerializer import StoreAddressSerializer




class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    

