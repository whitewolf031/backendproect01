from rest_framework import status, generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from proect.models import Proect, Category
from proect.permissons import IsOwnerOrReadOnly, IsAdminOrReadOnly
from proect.serializator import PersonSerializers

# bu pastdagi 3 classni ham bitdaga yozib olish usuli

# class ProectCRUD(viewsets.ModelViewSet):
#     queryset = Proect.objects.all()
#     serializer_class = PersonSerializers
#     permission_classes = (IsAdminUser,)
#


    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return Proect.objects.all()
    #
    #     return Proect.objects.filter(pk=pk)
    #
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     if pk:
    #         obj = Category.objects.get(pk=pk)
    #         return Response({"obj": obj.name})
    #     obj = Category.objects.all()
    #     return Response({"obj": [x.name for x in obj]})



#--------------------------------------------------------------------------------------------------

# bular pastdagi get, post, patch, put, Delete larga teng

#ListAPIView
# class Proectlist(generics.ListAPIView):
#     queryset = Proect.objects.all()
#     serializer_class = PersonSerializers

# CreateAPIView
# class ProectCreate(generics.CreateAPIView):
#     queryset = Proect.objects.all()
#     serializer_class = PersonSerializers


#Pagination
class PersonPagination(PageNumberPagination):
    page_size = 2 #Defoult pageda malumotlar sonini boshqarish
    page_size_query_param = 'page_size' #domen orqali pageda malumotlar sonini boshqarish  !important
    max_page_size = 3 #Pageda nechtagacha malumot chiqishi


# ListCreateAPIView
class ProectlistCreate(generics.ListCreateAPIView):
    queryset = Proect.objects.all()
    serializer_class = PersonSerializers
    permission_classes = (IsAuthenticated, )
    pagination_class = PersonPagination


# UpdateAPIView
class ProectUpdate(generics.RetrieveUpdateAPIView):
    queryset = Proect.objects.all()
    serializer_class = PersonSerializers
    permission_classes = (IsOwnerOrReadOnly, )


# DestroyAPIView
class ProectDestroy(generics.RetrieveDestroyAPIView):
    queryset = Proect.objects.all()
    serializer_class = PersonSerializers
    permission_classes = (IsAdminOrReadOnly, )


#----------------------------------------------------------------------------------------------------

# bular tepadagilarni yoyib yozilishi
# afzaligi bu yerda o'zimiz hoxlagancha shart yozsak boladi

# class ProectlistCreate(APIView):
    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if pk is not None:
    #         try:
    #             instance = Proect.objects.get(pk=pk)
    #
    #         except Proect.DoesNotExist:
    #             return Response({"Answer": "Data not found!"})
    #
    #         serializer = PersonSerializers(instance)
    #         return Response({"Answer": serializer.data})
    #
    #     else:
    #         list_person = Proect.objects.all()
    #         return Response({"People": PersonSerializers(list_person, many=True).data})
    #
    # def post(self, request):
    #     serializer = PersonSerializers(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"People": "It is work"})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if not pk:
    #         return Response({"Answer": "It is not found"})
    #
    #     try:
    #         instance = Proect.objects.get(pk=pk)
    #
    #     except:
    #         return Response("data not found")
    #
    #     serializers = PersonSerializers(data=request.data, instance=instance)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response({"Person": serializers.data})
    #
    # def patch(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if not pk:
    #         return Response({"Answer": "It is not found"})
    #
    #     try:
    #         instance = Proect.objects.get(pk=pk)
    #
    #     except:
    #         return Response("data not found")
    #
    #     serializers = PersonSerializers(data=request.data, instance=instance, partial=True)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response({"Person": serializers.data})
    #
    # def delete(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if not pk:
    #         return Response({"Delete is not work"})
    #
    #     try:
    #         instance = Proect.objects.get(pk=pk)
    #         instance.delete()
    #
    #     except:
    #         return Response("data not found")
    #
    #     return Response({"date": f"deleted - {pk}"})

