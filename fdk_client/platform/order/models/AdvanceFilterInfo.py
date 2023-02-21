"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FiltersInfo import FiltersInfo



from .FiltersInfo import FiltersInfo



from .FiltersInfo import FiltersInfo



from .FiltersInfo import FiltersInfo



from .FiltersInfo import FiltersInfo



class AdvanceFilterInfo(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    returned = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    unfulfilled = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    action_centre = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    processed = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
