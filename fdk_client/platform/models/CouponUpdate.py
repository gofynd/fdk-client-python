"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .Validation import Validation

from .Validity import Validity

from .RuleDefinition import RuleDefinition



from .CouponAction import CouponAction

from .CouponSchedule import CouponSchedule



from .State import State

from .Rule import Rule

from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    

