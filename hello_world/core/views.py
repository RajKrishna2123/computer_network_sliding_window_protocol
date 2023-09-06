from django.shortcuts import redirect, render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

# Create your views here.

# Create your views here.

def usr_inp(request):
    return  render(request ,"usr_inp.html")
def result(request):  
    return  render(request ,"login3.html")
def inp_chk(request):
    global frame_size,x,window_size
    temp=request.GET.get('frame_size','default')
    frame_size=int(temp)
    x=request.GET.get('binary_data','default')
    window_size=4
    s=0
    print(x)
    print(len(x))
    for i in range(0,len(x)):
        if (int(x[i])<=1):
            if (i==len(x)-1):
                return redirect('https://shiny-tribble-4v6pxvggg96c64g-8000.app.github.dev/inp_chk/sliding_win_protocol')                
            continue
        else:
            print("entered value is incorrect try again")            
            CONTEXT={"ERROR":"Previously Entered BINARY value was incorrect kindly retry"}
            return render(request,"usr_inp.html",CONTEXT)

def sliding_win_protocol(request):
    print(x)     
    y=[]
    temp=0
    pair=""
    for i in range(0,len(x)):
        if temp<frame_size:
            if i+1==len(x):
                pair=pair+x[i]
                temp=temp+1
                while temp<frame_size:
                    pair=pair+"#"
                    temp=temp+1
                y.append(pair)
            else:
                pair=pair+x[i]
                temp=temp+1        
        elif temp==frame_size:
            y.append(pair)
            temp=1
            pair=""
            pair=pair+x[i]
        else:
            y.append(pair)
            temp=0
            pair=""


    print(y)
    start=65
    name=[]
    packet_name_array=[]
    for i in range(0,len(y)):
        temp=chr(start)
        name.append(temp)
        start=start+1
    print(name)

    sender=y
    receiver=[]
    event_log=[]
    
    i=0
    send=4
    acknowledgement=0
    for i in range(0,len(y)+4):
        if i<window_size:
            receiver.append(sender[i])
            print("sent data ",name[i]," sucessfully containing ",sender[i])
            event_log.append("sent data "+name[i]+" sucessfully containing "+sender[i])
        elif i>=window_size:
            if (sender[acknowledgement]==receiver[acknowledgement] or i>len(y)):
                print("acknowledgment recieved for data ",name[acknowledgement]," containing ", sender[acknowledgement])
                event_log.append("acknowledgment recieved for data "+name[acknowledgement]+" containing "+sender[acknowledgement])
                acknowledgement=acknowledgement+1
                if (i<len(y)):
                    receiver.append(sender[i])
                    print("sent data ",name[i]," sucessfully containing ",sender[i] )
                    event_log.append("sent data "+name[i]+" sucessfully containing "+sender[i])
    received_data={}
    for i in range(0,len(sender)):
        received_data.update({name[i]:receiver[i]})
    print(received_data)
    print(event_log)
    context={"rawdata":event_log,"part":y}    
    return render(request ,"final_output.html",context)

def about(request):
    return render(request  ,"about.html")

def description(request):
    return render(request  ,"description.html")