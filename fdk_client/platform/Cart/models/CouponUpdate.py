"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .State import State



from .Restrictions import Restrictions



from .CouponAuthor import CouponAuthor



from .Identifier import Identifier



from .Validity import Validity



from .CouponSchedule import CouponSchedule



from .DisplayMeta import DisplayMeta



from .RuleDefinition import RuleDefinition



from .Ownership import Ownership





from .CouponAction import CouponAction





from .Validation import Validation



from .Rule import Rule





from .CouponDateMeta import CouponDateMeta



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
