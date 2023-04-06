"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .RuleDefinition import RuleDefinition



from .DisplayMeta import DisplayMeta

from .CouponAction import CouponAction

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .State import State

from .Ownership import Ownership

from .Rule import Rule

from .Restrictions import Restrictions

from .CouponAuthor import CouponAuthor

from .Validity import Validity

from .Validation import Validation



from .CouponSchedule import CouponSchedule


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    

