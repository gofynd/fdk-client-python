"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanyStoreView_PageItems import CompanyStoreView_PageItems





class CompanyStoreView_Response(BaseSchema):
    #  swagger.json

    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
