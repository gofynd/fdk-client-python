"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FollowIdsData import FollowIdsData



class FollowIdsResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(FollowIdsData, required=False)
    
