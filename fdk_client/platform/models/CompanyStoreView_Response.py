"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CompanyStoreView_PageItems import CompanyStoreView_PageItems


class CompanyStoreView_Response(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    

