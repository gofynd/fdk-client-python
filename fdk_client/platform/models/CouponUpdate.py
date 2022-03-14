"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta

from .Identifier import Identifier

from .Validation import Validation

from .CouponDateMeta import CouponDateMeta



from .Ownership import Ownership

from .Validity import Validity

from .RuleDefinition import RuleDefinition

from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule

from .CouponAction import CouponAction

from .Restrictions import Restrictions

from .State import State





from .Rule import Rule


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

