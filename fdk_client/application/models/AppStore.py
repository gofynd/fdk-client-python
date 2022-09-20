"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyStore import CompanyStore



from .StoreManagerSerializer import StoreManagerSerializer

from .SellerPhoneNumber import SellerPhoneNumber

from .StoreAddressSerializer import StoreAddressSerializer

from .StoreDepartments import StoreDepartments




class AppStore(BaseSchema):
    # Catalog swagger.json

    
    company = fields.Nested(CompanyStore, required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    name = fields.Str(required=False)
    

