"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CouponAuthor import CouponAuthor



from .State import State



from .DisplayMeta import DisplayMeta



from .Restrictions import Restrictions





from .Validity import Validity



from .Validation import Validation



from .RuleDefinition import RuleDefinition



from .Rule import Rule



from .CouponSchedule import CouponSchedule





from .CouponAction import CouponAction



from .Identifier import Identifier



from .Ownership import Ownership



from .CouponDateMeta import CouponDateMeta



class CouponAdd(BaseSchema):
    #  swagger.json

    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
