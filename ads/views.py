from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer

# Список объявлений с пагинацией и сортировкой
class AdListView(generics.ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        queryset = Ad.objects.all()

        # Параметры сортировки
        sort_by = self.request.query_params.get('sort_by', 'created_at')
        order = self.request.query_params.get('order', 'desc')

        if order == 'asc':
            queryset = queryset.order_by(sort_by)
        else:
            queryset = queryset.order_by(f'-{sort_by}')
        
        return queryset

# Получение одного объявления
class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

# Создание нового объявления
class AdCreateView(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    # Валидация данных (не больше 3 фото, длина названия и описания)
    def perform_create(self, serializer):
        if len(serializer.validated_data['photo_links']) > 3:
            raise serializers.ValidationError("Не более 3 ссылок на фото.")
        if len(serializer.validated_data['title']) > 200:
            raise serializers.ValidationError("Название не должно превышать 200 символов.")
        if len(serializer.validated_data['description']) > 1000:
            raise serializers.ValidationError("Описание не должно превышать 1000 символов.")

        serializer.save()
