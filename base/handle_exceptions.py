from datetime import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

from base import message_code
from base.exceptions import UserInvalidException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        details = exc.get_full_details()
        if isinstance(exc, ValidationError) or isinstance(exc, UserInvalidException):
            fields = _get_fields_error(details)
            message = fields[0]['message']
            system_code = exc.status_code
            error_code = fields[0]['apiErrorCode']
        else:
            fields = None,
            code = details['code']
            system_code, message = _get_error_details(code, None, None)
            error_code = system_code

        response.data = {
            'status': "ERROR",
            'body': None,
            'error': {
                'systemCode': system_code,
                'messageCode': error_code,
                'message': message,
                'trace': exc.detail,
                'timestamp': datetime.now(),
                'fields': fields if fields[0] is not None else None
            }
        }

    return response


def _get_error_details(code, message, field_name):
    try:
        err_code = message_code.ERROR_CODES[code]
        err_msg = message_code.ERROR_MESSAGES[code]

        if field_name in message_code.FIELDS:
            code = message_code.FIELDS[field_name]
            return code, message_code.ERROR_MESSAGES[code]

        return err_code, err_msg
    except Exception as _:
        return code, message


def _get_error(field_name, filed_code, message):
    e_code, e_msg = _get_error_details(filed_code, message, field_name)
    error = {
        'field': field_name,
        'rejectedValue': message,
        'apiErrorCode': e_code,
        'message': e_msg}
    return error


def _get_fields_error(full_details):
    fileds = []
    for field, details in full_details.items():
        if isinstance(details, dict):
            field_name = field
            message = details['message']
            code = details['code']
            error = _get_error(field_name, code, message)
            fileds.append(error)
        else:
            for d in details:
                try:
                    field_name = field if field != 'non_field_errors' else 'name'
                    message = d['message']
                    code = d['code']
                    error = _get_error(field_name, code, message)
                    fileds.append(error)
                except Exception as _:
                    error = _get_fields_error(d)
                    fileds.extend(error)
    return fileds
