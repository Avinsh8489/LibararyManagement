from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def BookList(request):
    print(f"\n\n\n\n\n >>>>>>>>>>>>>>>>>>>>>> {request} \n\n\n\n\n")

    color_list = """
    <!DOCTYPE html>
<html>
<body>

<h1 style="background-color:Tomato;">Python</h1>
<h1 style="background-color:Orange;">Java</h1>
<h1 style="background-color:DodgerBlue;">Node js</h1>
<h1 style="background-color:MediumSeaGreen;">React js</h1>
<h1 style="background-color:Gray;">Machine learning </h1>
<h1 style="background-color:SlateBlue;">Chat GPT </h1>
<h1 style="background-color:Violet;">HTML</h1>
<h1 style="background-color:LightGray;">JavaScript</h1>

</body>
</html>



"""
    return HttpResponse(color_list)