"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SellerPhoneNumber import SellerPhoneNumber



from .StoreAddressSerializer import StoreAddressSerializer

from .CompanyStore import CompanyStore



from .StoreDepartments import StoreDepartments

from .StoreManagerSerializer import StoreManagerSerializer


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

