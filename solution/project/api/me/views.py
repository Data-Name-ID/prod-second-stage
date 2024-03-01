import rest_framework.permissions
import rest_framework.response
import rest_framework.views


class ProfileView(rest_framework.views.APIView):
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def get(self, request):
        return rest_framework.response.Response(
            {
                'login': request.user.login,
                'email': request.user.email,
                'countryCode': request.user.countryCode,
                'isPublic': request.user.isPublic,
                'phone': request.user.phone,
                'image': request.user.image,
            },
            status=rest_framework.status.HTTP_200_OK,
        )
