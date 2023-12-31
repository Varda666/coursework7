# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
#
# from useful_habits.models import Course
# from useful_habits.permissions import IsModerator, IsOwner
# from useful_habits.serializers.course import CourseSerializer
# from rest_framework.permissions import IsAuthenticated
#
# from useful_habits.tasks import _send_mail_email
# from users.models import UserSubscriptionUpdates
#
#
# class CourseViewSet(ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [IsAuthenticated, IsModerator, IsOwner]
#
#     def partial_update(self, request, *args, **kwargs):
#         self.serializer_class = CourseSerializer(request.user, data=request.data, partial=True)
#         subscriptions = UserSubscriptionUpdates.objects.filter(course=request.course, status=True, many=True)
#         emails = subscriptions.values('email')
#         _send_mail_email(emails)
#         return Response(status=status.HTTP_202_ACCEPTED)
