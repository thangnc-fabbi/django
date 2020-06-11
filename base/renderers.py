from rest_framework.renderers import JSONRenderer


class EmberJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data and 'error' in data and data['error']:
            data = {'status': data['status'],
                    'body': data['body'],
                    'error': data['error']}
        elif data and 'links' in data and data['links']:
            data = {
                'status': 'OK',
                'body': data['data'],
                'error': None,
                'links': data['links']
            }
        else:
            data = {'status': 'OK',
                    'body': data,
                    'error': None}
        return super(EmberJSONRenderer, self).render(data, accepted_media_type, renderer_context)
