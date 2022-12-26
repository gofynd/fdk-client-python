"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership import Ownership

from .Restrictions import Restrictions

from .Rule import Rule

from .CouponAction import CouponAction



from .Validity import Validity



from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Validation import Validation

from .State import State

from .Identifier import Identifier

from .RuleDefinition import RuleDefinition




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

