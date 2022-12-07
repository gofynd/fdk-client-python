"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .JioCodeUpsertDataSet import JioCodeUpsertDataSet



class JioCodeUpsertPayload(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(JioCodeUpsertDataSet, required=False), required=False)
    
