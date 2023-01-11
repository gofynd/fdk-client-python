"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RuleDefinition import RuleDefinition



from .CouponSchedule import CouponSchedule





from .Validation import Validation



from .Restrictions import Restrictions





from .State import State



from .CouponAction import CouponAction



from .Validity import Validity



from .Rule import Rule



from .CouponAuthor import CouponAuthor





from .Ownership import Ownership



from .Identifier import Identifier



from .CouponDateMeta import CouponDateMeta



from .DisplayMeta import DisplayMeta



class CouponUpdate(BaseSchema):
    #  swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
