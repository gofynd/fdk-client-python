"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OtherSellerApplication import OtherSellerApplication



from .Page import Page



class OtherSellerApplications(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(OtherSellerApplication, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
