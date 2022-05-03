from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myApp.models import Employeedata

# Create your views here.
#Her i am Creating two functions one is home def home is get the input and redirsct to the home.html
def hometwo(request):
    #in django we have two methods one is get and post her get data through request.method=="GET"
    if request.method=="GET":
        #get data stored in the output in the from of srting(get("output"))
        output=request.GET.get('output')
        #here return the output in to home.html myApp is folder in templates
        return render(request, "myApp/home.html", {"output": output})


def home(request):
    #in django we have two methods one is get and post her get data through request.method=="GET"
    if request.method=="GET":
        #get data stored in the output in the from of srting(get("output"))
        output=request.GET.get('output')
        #here return the output in to home.html myApp is folder in templates
        return render(request, "myApp/home.html", {"output": output})


#second functions in views and main code part checking employee data
def EmployeeCheck(request):
    #here str declering as global vareble we can use any wher in the function
    global str
    #here c declering as global vareble we can use any wher in the function
    global c
    #c is vareble
    c = 0
    #hh is vareble for storin string data
    hh=''
    #pylist is python list
    pylist =["20220314001", "20220314002", "20220314003", "20220314004", "20220314005"]
    #pydict is dictionry of python
    pydict={"20220314001" : "Ram", "20220314002" : "Sam", "20220314003" : "Rada", "20220314004":"Rani", "20220314005":"govinda"}
    #Here strlist is main part of code post data from input cath the data through the post method and it convert into str in the from of string
    strlist = str(request.POST["python1"])
    #here i am calling Employeedata calss from models.py and assigning class to Data1
    Data1 = Employeedata()
    #Here I am assigning string type of "sri rama" to the class object of Data.name
    Data1.name = "Sri Rama"
    #Here I am assigning string type of "20220314001" to the class object of Data.name
    Data1.empid = "20220314001"

    #here i am calling Employeedata calss from models.py and assigning class to Data2
    Data2 = Employeedata()
    #Here I am assigning string type of "sri Vishnua" to the class object of Data.name
    Data2.name = "Sri Vishnua"
    #Here I am assigning string type of "20220314002" to the class object of Data.name
    Data2.empid = "20220314002"

    #here i am calling Employeedata calss from models.py and assigning class to Data3
    Data3 = Employeedata()
    #Her I am assigning string type of "sri Hari" to the class object of Data.name
    Data3.name = "Sri Hari"
    #Here I am assigning string type of "20220314003" to the class object of Data.name
    Data3.empid = "20220314003"

    #here i am calling Employeedata calss from models.py and assigning class to Data4
    Data4 = Employeedata()
    #Her I am assigning string type of "Srivalli" to the class object of Data.name
    Data4.name = "Srivalli "
    #Here I am assigning string type of "20220314004" to the class object of Data.name
    Data4.empid = "20220314004"

    #here i am calling Employeedata calss from models.py and assigning class to Data5
    Data5 = Employeedata()
    #Here I am assigning string type of "sri Lakshmi" to the class object of Data.name
    Data5.name = "Sri Lakshmi"
    #Here I am assigning string type of "20220314005" to the class object of Data.name
    Data5.empid = "20220314005"

    #here i am calling Employeedata calss from models.py and assigning class to Data0
    Data00 = Employeedata()
    #Here I am assigning string type of "non" to the class object of Data.name
    Data00.name = strlist
    #Here I am assigning string type of "non" to the class object of Data.name
    Data00.empid = "non"
    #as mention above #Her strlist is main part of code post data from input cath the data through the post method and it convert into str in the from of string
    strlist = str(request.POST["python1"])
    #Here strlist is cheeking python list of pylist
    if strlist == "20220314001":
        #here if condetion is satesfive the condetion c will store the 1
        c=1
        # Data1 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data1
    #Her strlist is cheeking python list of pylist
    elif strlist == "20220314002":
        #here elif condetion is satesfive the condetion c will store the 1
        c=1
        # Data2 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data2
     #Her strlist is cheeking python list of pylist
    elif strlist == "20220314003":
        #here elif condetion is satesfive the condetion c will store the 1
        c=1
        # Data3 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data3
    #Her strlist is cheeking python list of pylist
    elif strlist == "20220314004":
        #here elif condetion is satesfive the condetion c will store the 1
        c=1
        # Data4 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data4
    #Here strlist is cheeking python list of pylist
    elif strlist == "20220314005":
        #here elif condetion is satesfive the condetion c will store the 1
        c=1
        # Data5 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data5

    #Here if c==1 any of above functions c==1 then only sm is print in the frentend part
    if c==1:
        sm=" Successfully provide issued to+"+" "+ db.name+" "+"and ID is "+ db.empid +".  "
    #Here c!=1 else db = Data00 will print
    else:
        # Data00 is assigning to the db and if condetion satisfives the db will print in frentend
        db = Data00
        sm="Not successful ID  "+" "+db.name+"."
    #here return the output in to home.html myApp is folder in templates
    return HttpResponseRedirect("/hometwo/?output={}".format(sm))


    """strlist = str(request.POST["python1"])
    n={}
    for k,v in pydict.items():
        for list in pylist:
            if list == strlist and k==list:
                c=1
                hh=list
                n[k]=v
                bb=n[k]
                break
    if c==1:
        EmpDataB(request)
        sm="Document Code verification successful provide Issued To" +"  "+ hh + "  "+bb + "  "+"For any details please reach out to hr@widesigninc.com"
        return HttpResponseRedirect("/home/?output={}".format(ms))
    else:
        sm="not successful Please reach out to hr@widesigninc.com for additional details"
        return HttpResponse("/home/?output={}".format(sm))
    return HttpResponseRedirect("/home/?output={}".format(sm))"""



"""def EmpDataB(request):
    Data1 = Employeedata()
    name = "SriRama"
    empid = "20220314001"
    Data2 = Employeedata()
    name = "SriRama"
    empid = "20220314002"
    Data3 = Employeedata()
    name = "SriRama"
    empid = "20220314003"
    Data4 = Employeedata()
    name = "SriRama"
    empid = "20220314004"
    Data5 = Employeedata()
    name = "SriRama"
    empid = "20220314005"
    Data00 = Employeedata()
    name = ""
    empid = ""
    strlist = EmployeeCheck()
    if strlist == "20220314001":
        db = Data1
    elif strlist == "20220314002":
        db = Data2
    elif strlist == "20220314003":
        db = Data3
    elif strlist == "20220314004":
        db = Data4
    elif strlist == "20220314005":
        db = Data5
    else:
        db = Data00
    return render(request, "myApp/result.html", {"db":db})"""
