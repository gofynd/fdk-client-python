"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Ownership import Ownership



from .Rule import Rule



from .Validation import Validation



from .CouponAuthor import CouponAuthor



from .CouponDateMeta import CouponDateMeta



from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule



from .RuleDefinition import RuleDefinition



from .DisplayMeta import DisplayMeta



from .Identifier import Identifier





from .State import State







from .Restrictions import Restrictions



from .Validity import Validity



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
