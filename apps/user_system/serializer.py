from djoser.serializers import UserCreateSerializer
from apps.user_system.models import Model_users

class ModelUserDjoserSerializers (UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Model_users
        fields = ["username", "img"]