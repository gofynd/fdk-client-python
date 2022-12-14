"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .State import State

from .CouponSchedule import CouponSchedule

from .Validity import Validity

from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier



from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .Rule import Rule

from .Validation import Validation


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    

