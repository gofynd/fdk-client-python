"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .RuleDefinition import RuleDefinition

from .Rule import Rule

from .CouponSchedule import CouponSchedule



from .Ownership import Ownership

from .State import State

from .Restrictions import Restrictions



from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta

from .Validation import Validation


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    

