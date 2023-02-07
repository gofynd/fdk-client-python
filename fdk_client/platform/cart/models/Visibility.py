"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Visibility(BaseSchema):
    #  swagger.json

    
    pdp = fields.Boolean(required=False)
    
    coupon_list = fields.Boolean(required=False)
    
