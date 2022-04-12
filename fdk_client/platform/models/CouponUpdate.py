"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponDateMeta import CouponDateMeta

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta

from .Identifier import Identifier

from .State import State

from .Rule import Rule

from .Validity import Validity

from .Validation import Validation

from .RuleDefinition import RuleDefinition






class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

