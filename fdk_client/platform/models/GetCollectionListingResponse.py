"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetCollectionDetailNest import GetCollectionDetailNest

from .CollectionListingFilter import CollectionListingFilter

from .Page import Page


class GetCollectionListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    page = fields.Nested(Page, required=False)
    

