"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DomainSuggestion import DomainSuggestion



class DomainSuggestionsResponse(BaseSchema):
    #  swagger.json

    
    domains = fields.List(fields.Nested(DomainSuggestion, required=False), required=False)
    
