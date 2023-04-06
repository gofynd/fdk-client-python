"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreTiming import StoreTiming

from .CompanyStore import CompanyStore







from .StoreManagerSerializer import StoreManagerSerializer

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreDepartments import StoreDepartments

from .SellerPhoneNumber import SellerPhoneNumber


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    

