"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FiltersInfo import FiltersInfo



from .AdvanceFilterInfo import AdvanceFilterInfo



class FiltersResponse(BaseSchema):
    #  swagger.json

    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    advance_filter = fields.Nested(AdvanceFilterInfo, required=False)
    
