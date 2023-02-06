"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CustomForm import CustomForm



from .Page import Page



class CustomFormList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CustomForm, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
