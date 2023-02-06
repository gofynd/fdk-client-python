"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponSchedule import CouponSchedule



from .Ownership import Ownership



from .CouponAction import CouponAction



from .State import State





from .CouponAuthor import CouponAuthor



from .RuleDefinition import RuleDefinition



from .Restrictions import Restrictions



from .Validity import Validity



from .DisplayMeta import DisplayMeta



from .CouponDateMeta import CouponDateMeta





from .Rule import Rule



from .Identifier import Identifier



from .Validation import Validation





class CouponUpdate(BaseSchema):
    #  swagger.json

    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
