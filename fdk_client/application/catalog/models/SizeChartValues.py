"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class SizeChartValues(BaseSchema):
    #  swagger.json

    
    col_4 = fields.Str(required=False)
    
    col_5 = fields.Str(required=False)
    
    col_2 = fields.Str(required=False)
    
    col_6 = fields.Str(required=False)
    
    col_1 = fields.Str(required=False)
    
    col_3 = fields.Str(required=False)
    
