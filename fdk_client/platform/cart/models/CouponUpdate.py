"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CouponDateMeta import CouponDateMeta



from .Identifier import Identifier



from .Validity import Validity



from .CouponAction import CouponAction





from .Ownership import Ownership





from .RuleDefinition import RuleDefinition



from .State import State



from .Validation import Validation



from .CouponSchedule import CouponSchedule



from .CouponAuthor import CouponAuthor



from .DisplayMeta import DisplayMeta





from .Restrictions import Restrictions



from .Rule import Rule



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
