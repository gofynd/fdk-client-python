"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    # OrderManage swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    

