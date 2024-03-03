import rest_framework.response
import rest_framework.status
import rest_framework.views


class PingView(rest_framework.views.APIView):
    def get(self, request, format=None):
        return rest_framework.response.Response(
            'ok', status=rest_framework.status.HTTP_200_OK,
        )
