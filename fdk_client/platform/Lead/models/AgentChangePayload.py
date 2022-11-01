"""Lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AgentChangePayload(BaseSchema):
    #  swagger.json

    
    agent_id = fields.Str(required=False)
    
