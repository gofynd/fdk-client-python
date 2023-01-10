"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Validation import Validation



from .State import State





from .Ownership import Ownership



from .CouponSchedule import CouponSchedule





from .Identifier import Identifier



from .Validity import Validity





from .Rule import Rule



from .DisplayMeta import DisplayMeta



from .CouponAuthor import CouponAuthor



from .CouponAction import CouponAction



from .CouponDateMeta import CouponDateMeta



from .RuleDefinition import RuleDefinition



from .Restrictions import Restrictions



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
