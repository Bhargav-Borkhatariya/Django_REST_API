from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Employee_CRUD.models import Employee
from Employee_CRUD.serializers import EmployeeSerializer


class EmployeeApiView(APIView):
    """
    Here you can find the get, post, put and detele method code,
    that all have seprate function for work,
    we use serializer for parsing data to jason and send that with response.
    """
    # get function.
    def get(self, request, pk=None):
        """
        if have id then return only that id data,
        Either send all data.
        """
        if pk:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            data = serializer.data
            content = {'data': data, 'message': 'Data Get Successfully'}
            return Response(data=content)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            data = serializer.data
            content = {'data': data, 'message': 'Data Get Successfully'}
            return Response(data=content)

    # Post method.
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            content = {'data': data, 'message': 'Data Post Successfully'}
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Put method.
    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            content = {'data': data, 'message': 'Data Put Successfully'}
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete method.
    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        data = {'message': 'Data DELETE Successfully'}
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
