"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DisplayMeta import DisplayMeta





from .Identifier import Identifier



from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule





from .Restrictions import Restrictions



from .CouponDateMeta import CouponDateMeta



from .State import State



from .CouponAuthor import CouponAuthor



from .Validity import Validity



from .RuleDefinition import RuleDefinition



from .Ownership import Ownership



from .Validation import Validation



from .Rule import Rule



class CouponAdd(BaseSchema):
    #  swagger.json

    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
