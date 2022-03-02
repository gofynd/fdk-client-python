"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SellerPhoneNumber import SellerPhoneNumber

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreTiming import StoreTiming

from .CompanyStore import CompanyStore



from .StoreDepartments import StoreDepartments



from .StoreManagerSerializer import StoreManagerSerializer


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

