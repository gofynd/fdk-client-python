"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AdvanceFilterInfo import AdvanceFilterInfo



from .FiltersInfo import FiltersInfo



class FiltersResponse(BaseSchema):
    #  swagger.json

    
    advance_filter = fields.Nested(AdvanceFilterInfo, required=False)
    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
