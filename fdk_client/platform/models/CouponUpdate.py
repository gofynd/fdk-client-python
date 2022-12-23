"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rule import Rule



from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta



from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions

from .Identifier import Identifier

from .Ownership import Ownership

from .Validation import Validation

from .CouponAction import CouponAction

from .State import State




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

