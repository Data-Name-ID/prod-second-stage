import rest_framework.response
import rest_framework.views


class PingView(rest_framework.views.APIView):
    http_method_names = ('get',)

    def get(self, request, format=None):
        return rest_framework.response.Response('ok', status=200)