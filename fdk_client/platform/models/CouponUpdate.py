"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Restrictions import Restrictions

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .State import State

from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .CouponAuthor import CouponAuthor



from .Validity import Validity

from .Ownership import Ownership

from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta



from .Rule import Rule

from .CouponAction import CouponAction


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    

