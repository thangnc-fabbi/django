from base import constants
from django.utils.translation import gettext as _

ERROR_MESSAGES = {
    constants.ERR_BAD_REQUEST: _('Bad request.'),
    constants.ERR_INVALID_TYPE: _('Invalid Type.'),
    constants.ERR_NOT_BLANK: _('This field is not blank.'),
    constants.ERR_NOT_AUTHENTICATED: _('Authenticated False.'),
    constants.ERR_RESOURCE_MAX_SIZE: _('Resource max size.'),
    constants.ERR_UNIQUE_FIELD: _('Item already exists.'),
    constants.ERR_RESOURCE_NOT_FOUND: _('Resource not found.'),
    constants.ERR_PERMISSION_DENIED: _('Permission denied.'),
}

ERROR_CODES = {
    constants.ERR_BAD_REQUEST: 'ERR_BAD_REQUEST',
    constants.ERR_INVALID_TYPE: 'ERR_INVALID_TYPE',
    constants.ERR_NOT_BLANK: _('ERR_NOT_BLANK'),
    constants.ERR_NOT_AUTHENTICATED: _('ERR_NOT_AUTHENTICATED'),
    constants.ERR_RESOURCE_MAX_SIZE: _('ERR_RESOURCE_MAX_SIZE'),
    constants.ERR_UNIQUE_FIELD: _('ERR_UNIQUE_FIELD'),
    constants.ERR_RESOURCE_NOT_FOUND: _('ERR_RESOURCE_NOT_FOUND'),
    constants.ERR_PERMISSION_DENIED: _('ERR_PERMISSION_DENIED'),
}

FIELDS = {
}
