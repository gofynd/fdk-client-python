"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SellerPhoneNumber import SellerPhoneNumber

from .StoreDepartments import StoreDepartments

from .StoreManagerSerializer import StoreManagerSerializer

from .CompanyStore import CompanyStore

from .StoreAddressSerializer import StoreAddressSerializer


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    

