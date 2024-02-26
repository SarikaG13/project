from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber = data.get('textfirstnumber')
        secondnumber = data.get('textsecondnumber')
        if('buttonadd' in request.POST):
            result=int(firstnumber )+ int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttonsub' in request.POST):
            result=int(firstnumber )+ int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttonmul' in request.POST):
            result=int(firstnumber )+ int(secondnumber)
            return render(request,'calci.html',context={'result':result})
        if('buttondiv' in request.POST):
            result=int(firstnumber )+ int(secondnumber)
            return render(request,'calci.html',context={'result':result})
    return render(request,'calci.html')

def index(request):
    return render(request,'index.html')

def drink(request):
    if(request.method=="POST"):
        data=request.POST
        age=data.get('textage')
        height=data.get('textheight')
        weight=data.get('textweight')
        waist=data.get('textwaist')
        eyesightl=data.get('texteyesightl')
        eyesightr=data.get('texteyesightr')
        hearingl=data.get('texthearingl')
        hearingr=data.get('texthearingr')
        systolic=data.get('textsystolic')
        relaxation=data.get('textrelaxation')
        fastingbloodsugar=data.get('textfastingbloodsugar')
        cholesterol=data.get('textcholesterol')
        trigylceride=data.get('texttriglyceride')
        hdl=data.get('texthdl')
        ldl=data.get('textldl')
        hemoglobin=data.get('texthemoglobin')
        urineprotein=data.get('texturineprotein')
        serumcreatinine=data.get('textserumcreatinine')
        ast=data.get('textast')
        alt=data.get('textalt')
        gtp=data.get('textgtp')
        dentalcaries=data.get('textdentalcaries')
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\Dell\\Desktop\\Batch_04\\Data\\train_dataset.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())

            inputs=data.drop('smoking',axis=1)
            output=data['smoking']

            #print(inputs)
            #print(output)

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            #print(y_pred)
            #print(y_test)

            result=model.predict([[int(age),int(height),int(weight),float(waist),float(eyesightl),float(eyesightr),int(hearingl),int(hearingr),int(systolic),int(relaxation),int(fastingbloodsugar),int(cholesterol),int(trigylceride),int(hdl),int(ldl),float(hemoglobin),int(urineprotein),float(serumcreatinine),int(ast),int(alt),int(gtp),int(dentalcaries)]])
            print(result)
            if result==1:
                return HttpResponse("the person is smoking")
            else:
                return HttpResponse("the person is not smoking")
        return render(request,'drink.html',context={'result':result})
    
    return render(request,'drink.html')



    