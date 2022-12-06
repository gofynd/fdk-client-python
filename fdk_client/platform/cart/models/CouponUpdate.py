"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Validity import Validity





from .Identifier import Identifier





from .CouponSchedule import CouponSchedule



from .RuleDefinition import RuleDefinition



from .State import State



from .Restrictions import Restrictions



from .Validation import Validation





from .CouponDateMeta import CouponDateMeta



from .Rule import Rule



from .CouponAuthor import CouponAuthor



from .CouponAction import CouponAction



from .Ownership import Ownership



from .DisplayMeta import DisplayMeta



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
