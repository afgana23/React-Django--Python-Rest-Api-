from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer,serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
#viewset based api
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import status
#generic view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
#session authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser




# Create your views here.
def home(request):
  cust=Customer.objects.all()
 
  serilizer=CustomerSerializer(cust, many=True)
  filter=[SearchFilter]
  searh=['address']
  json_data=JSONRenderer().render(serilizer.data)
  return HttpResponse(json_data,content_type='application/json')





  #return render(request,"index.html")
def infoapi(request,pk):
  cust=Customer.objects.get(id=pk)
  serilizer=CustomerSerializer(cust)
  #json_data=JSONRenderer().render(serilizer.data)
  #return HttpResponse(json_data,content_type='application/json')
  return JsonResponse(serilizer.data)

@csrf_exempt
def customer_add(request):
  #if request.method =='POST':
    json_data=request.body
    stream=io.BytesIO(json_data)
    pythondata= JSONParser().parse(stream)
    sezer=CustomerSerializer(data=pythondata)
    if sezer.is_valid():
      sezer.save()
      res={'msg':'creates datas'}
      json_data=JSONRenderer().render(res)
    return HttpResponse(json_data,content_type='application/json')
#return JsonResponse(sezer.data)



#function based api
#@api_view()
#def fun_api(request):
 #  return Response({'msg':"hello afgghhh"})
#@api_view(['POST'])
#def fun_api(request):
 # if request.method=='POST':
   #print(request.data)
  # return Response({'msg':"hello POST"})


@api_view(['GET','POST'])
def fun_api(request):
  if request.method=='GET':
   #print(request.data)
   return Response({'msg':"hello get method"})


  if request.method=='POST':
   #print(request.data)
   return Response({'msg':"hello POST",'data':request.data})
  
  
  #crud through function based Api
@api_view(['GET','POST','PUT','DELETE'])

def crud_api(request):
  if request.method=='GET':
    id=request.data.get('id')
    if id is not None:
      cust=Customer.objects.get(id=id)
      serializer=CustomerSerializer(cust)
      return Response(serializer.data)
    cust=Customer.objects.all()
    serializer=CustomerSerializer(cust,many=True)
    return Response(serializer.data)
  if request.method=='POST':
    serializer=CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'data created'})
    return Response(serializer.errors)
  if request.method=='PUT':
    id=request.data.get('id')
    cust=Customer.objects.get(id=id)
    serializer=CustomerSerializer(cust, data=request.data,partial=True)
    
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'data Updated'})
    return Response(serializer.errors)
  if request.method=='DELETE':
    id=request.data.get('id')
    cust=Customer.objects.get(id=id)
    cust.delete()
    return Response({'msg':'data deleted'})
    #return Response(serializer.errors)
class custViewSet(viewsets.ViewSet):
  def List(self,request):
    custm=Customer.objects.all()
    serializer=CustomerSerializer(custm,many=True)
    return Response(serializer.data)
  def retrive(self,request,pk=None):
    id=pk
    if id is not None:
      cust=Customer.objects.get(id=id)
      serializer=CustomerSerializer(cust)
      return Response(serializer.data)


#class based api     
class CustomerApi(APIView):
  def get(self,request,pk=None,format=None):
    id=pk
    if id is not None:
      cst=Customer.objects.get(id=id)
      serializer=CustomerSerializer(cst)
      return Response(serializer.data)
    cst=Customer.objects.all()
    serializer=CustomerSerializer(cst,many=True)
    return Response(serializer.data)
  def post(self,request,format=None):
      serializer=CustomerSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':"data created"},status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
  #Generic api
class DataList(GenericAPIView,ListModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def get(self,request,*args,**kwargs):
      return self.list(request,*args,**kwargs)

class CreateDataList(GenericAPIView,CreateModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def post(self,request,*args,**kwargs):
      return self.create(request,*args,**kwargs)    


class RetrieveDataList(GenericAPIView,RetrieveModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)       


class UpdateDataList(GenericAPIView,UpdateModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)   
 #Generic api with single urls   
class DataListtogether(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def get(self,request,*args,**kwargs):
      return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
      return self.create(request,*args,**kwargs)    
    #xxxxxxxxxxxxxxxxxxx---------------------generic view ---------------------xxxxxxxxxxxxxxx

    #ViewSet api method
class NewDataview(viewsets.ViewSet):
  def list(self,request):
    stm=Customer.objects.all()
    serializer=CustomerSerializer(stm,many=True)
    return Response(serializer.data)
  def retrieve(self,request,pk=None):
    id=pk
    if id is not None:
      cust=Customer.objects.get(id=id)
      serializer=CustomerSerializer(cust)
      return Response(serializer.data)
    def create(self,request):

      serializer=CustomerSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()


      return Response({'msg':"ctested"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
 #xxxxxxxxxxxxxxxxxxxx----------ViewSet api method---xxxxxxxxxxxxxxxx
  
class secureview(viewsets.ModelViewSet):
  queryset=Customer.objects.all()
  serializer_class=CustomerSerializer
  authentication_classes=[SessionAuthentication]
  permission_classes=[IsAuthenticated]  
  permission_classes=[IsAdminUser]  
        

    



    


  

