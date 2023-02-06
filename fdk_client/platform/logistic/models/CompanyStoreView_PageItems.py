"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CompanyStoreView_PageItems(BaseSchema):
    #  swagger.json

    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
