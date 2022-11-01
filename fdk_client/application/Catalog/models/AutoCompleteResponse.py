"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AutocompleteItem import AutocompleteItem



class AutoCompleteResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    
