"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionPrice import CollectionPrice





from .CollectionPrice import CollectionPrice








class CollectionQuery1(BaseSchema):
    # Catalog swagger.json

    
    image_nature = fields.List(fields.Str(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    genders = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(CollectionPrice, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    discount = fields.Nested(CollectionPrice, required=False)
    
    categories = fields.List(fields.Int(required=False), required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    

