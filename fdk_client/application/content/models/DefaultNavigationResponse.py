"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .NavigationSchema import NavigationSchema



class DefaultNavigationResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
