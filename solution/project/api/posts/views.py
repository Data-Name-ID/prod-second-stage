import rest_framework.permissions
import rest_framework.response
import rest_framework.status
import rest_framework.views

import api.posts.models
import api.posts.serializers
import api.utils


class AddPostView(rest_framework.views.APIView):
    http_method_names = ('post',)
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    def post(self, request):
        serializer = api.posts.serializers.PostSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            post = serializer.save()

            tag_names = request.data.get('tags')

            if tag_names:
                for tag_name in tag_names:
                    tag, _ = api.posts.models.Tag.objects.get_or_create(
                        name=tag_name,
                    )
                    tag.posts.add(post)
                    tag.save()

            return rest_framework.response.Response(
                serializer.data,
                status=rest_framework.status.HTTP_201_CREATED,
            )

        return api.utils.get_error_response(serializer)
