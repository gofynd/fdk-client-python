"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RuleDefinition import RuleDefinition



from .Ownership import Ownership



from .CouponDateMeta import CouponDateMeta





from .CouponSchedule import CouponSchedule



from .Validity import Validity



from .Rule import Rule



from .DisplayMeta import DisplayMeta



from .Validation import Validation



from .Restrictions import Restrictions



from .CouponAction import CouponAction





from .Identifier import Identifier





from .CouponAuthor import CouponAuthor



from .State import State



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
