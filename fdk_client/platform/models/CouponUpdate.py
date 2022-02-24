"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition

from .Identifier import Identifier



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta



from .DisplayMeta import DisplayMeta

from .CouponSchedule import CouponSchedule

from .Validity import Validity



from .State import State

from .Rule import Rule

from .CouponAction import CouponAction

from .Ownership import Ownership

from .Restrictions import Restrictions

from .Validation import Validation


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    

