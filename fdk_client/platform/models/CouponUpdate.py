"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier

from .CouponSchedule import CouponSchedule

from .Validation import Validation

from .CouponAction import CouponAction

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity



from .State import State

from .CouponAuthor import CouponAuthor



from .RuleDefinition import RuleDefinition

from .Ownership import Ownership

from .Rule import Rule

from .DisplayMeta import DisplayMeta



from .Restrictions import Restrictions


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    

