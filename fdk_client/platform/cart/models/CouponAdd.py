"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .State import State



from .Ownership import Ownership



from .Validation import Validation



from .CouponAuthor import CouponAuthor





from .CouponAction import CouponAction



from .Identifier import Identifier





from .CouponDateMeta import CouponDateMeta



from .DisplayMeta import DisplayMeta



from .RuleDefinition import RuleDefinition



from .Rule import Rule





from .Validity import Validity



from .Restrictions import Restrictions



from .CouponSchedule import CouponSchedule



class CouponAdd(BaseSchema):
    #  swagger.json

    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
