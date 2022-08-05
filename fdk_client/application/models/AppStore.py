"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SellerPhoneNumber import SellerPhoneNumber



from .CompanyStore import CompanyStore

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreManagerSerializer import StoreManagerSerializer



from .StoreDepartments import StoreDepartments


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    

