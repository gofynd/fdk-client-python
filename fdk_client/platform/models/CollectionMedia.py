"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BannerImage import BannerImage

from .CustomBanner import CustomBanner




class CollectionMedia(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Dict(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    custombanner = fields.List(fields.Nested(CustomBanner, required=False), required=False)
    
    landscape = fields.Dict(required=False)
    

