from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item  # Import the ToDoList and Item models
from .forms import CreateNewList


# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):  # get button have name is Save
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):  # get button have name is newItem
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

def home(request):
    return render(request, 'main/home.html', {'user': request.user})

def create(response):
    t = None
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            if response.user:
                response.user.todolist.add(t)
                return HttpResponseRedirect("/%i" % t.id)
            else:
                return HttpResponse("User not found")
        else:
            return HttpResponse("Invalid form data")
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})

def view(response):
	return render(response, "main/view.html")