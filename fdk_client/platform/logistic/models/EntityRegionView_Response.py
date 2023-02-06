"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EntityRegionView_Items import EntityRegionView_Items





from .EntityRegionView_Error import EntityRegionView_Error



from .EntityRegionView_page import EntityRegionView_page



class EntityRegionView_Response(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    
