"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionImage import CollectionImage

from .CustomBanner import CustomBanner

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage


class CollectionBanner(BaseSchema):
    # Catalog swagger.json

    
    landscape_web = fields.Nested(CollectionImage, required=False)
    
    custombanner = fields.List(fields.Nested(CustomBanner, required=False), required=False)
    
    landscape_mobile = fields.Nested(CollectionImage, required=False)
    
    portrait_mobile = fields.Nested(CollectionImage, required=False)
    
    portrait_web = fields.Nested(CollectionImage, required=False)
    

