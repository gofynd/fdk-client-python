"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage


class CollectionBanner(BaseSchema):
    # Catalog swagger.json

    
    portrait_mobile = fields.Nested(CollectionImage, required=False)
    
    landscape_mobile = fields.Nested(CollectionImage, required=False)
    
    landscape_web = fields.Nested(CollectionImage, required=False)
    
    custombanner = fields.List(fields.Nested(CollectionImage, required=False), required=False)
    
    portrait_web = fields.Nested(CollectionImage, required=False)
    

