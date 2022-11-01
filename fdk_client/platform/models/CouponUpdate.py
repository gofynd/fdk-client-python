"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAction import CouponAction

from .Rule import Rule

from .CouponSchedule import CouponSchedule



from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .CouponAuthor import CouponAuthor

from .Validity import Validity

from .CouponDateMeta import CouponDateMeta





from .Identifier import Identifier

from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .State import State

from .Ownership import Ownership


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    

