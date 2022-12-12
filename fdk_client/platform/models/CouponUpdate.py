"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation



from .Restrictions import Restrictions

from .CouponSchedule import CouponSchedule

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .CouponAction import CouponAction

from .Identifier import Identifier





from .State import State

from .Ownership import Ownership


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    

