"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .Ownership import Ownership

from .CouponSchedule import CouponSchedule



from .State import State

from .Rule import Rule



from .Validation import Validation

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction

from .RuleDefinition import RuleDefinition

from .CouponAuthor import CouponAuthor




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    

