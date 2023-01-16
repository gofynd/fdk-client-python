"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Restrictions import Restrictions





from .CouponSchedule import CouponSchedule





from .CouponDateMeta import CouponDateMeta



from .Ownership import Ownership



from .RuleDefinition import RuleDefinition



from .CouponAuthor import CouponAuthor



from .CouponAction import CouponAction



from .DisplayMeta import DisplayMeta



from .State import State



from .Validation import Validation



from .Rule import Rule



from .Identifier import Identifier





from .Validity import Validity



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
