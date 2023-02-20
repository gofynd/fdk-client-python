"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponSchedule import CouponSchedule





from .Identifier import Identifier





from .CouponAuthor import CouponAuthor



from .Validity import Validity



from .Ownership import Ownership





from .CouponDateMeta import CouponDateMeta



from .CouponAction import CouponAction



from .Restrictions import Restrictions



from .State import State



from .Rule import Rule



from .Validation import Validation



from .RuleDefinition import RuleDefinition



from .DisplayMeta import DisplayMeta



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
