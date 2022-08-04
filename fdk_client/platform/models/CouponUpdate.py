"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation

from .Ownership import Ownership

from .CouponAction import CouponAction

from .State import State

from .Validity import Validity

from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .CouponAuthor import CouponAuthor



from .Rule import Rule





from .Identifier import Identifier

from .RuleDefinition import RuleDefinition


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    

