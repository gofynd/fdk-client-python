"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ColumnHeader import ColumnHeader



from .ColumnHeader import ColumnHeader



from .ColumnHeader import ColumnHeader



from .ColumnHeader import ColumnHeader



from .ColumnHeader import ColumnHeader



from .ColumnHeader import ColumnHeader



class ColumnHeaders(BaseSchema):
    #  swagger.json

    
    col_4 = fields.Nested(ColumnHeader, required=False)
    
    col_3 = fields.Nested(ColumnHeader, required=False)
    
    col_5 = fields.Nested(ColumnHeader, required=False)
    
    col_6 = fields.Nested(ColumnHeader, required=False)
    
    col_2 = fields.Nested(ColumnHeader, required=False)
    
    col_1 = fields.Nested(ColumnHeader, required=False)
    
