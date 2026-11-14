drop,count,i=0,0,0
cap=int(input("Enter the bucket size: "))
process=int(input("Enter the processing rate: "))
nsec=int(input("Enter the number of seconds you want to simulate: "))
inp=[]
for i in range(nsec):
    temp=int(input(f"Enter the size of packet entering at {i+1} sec: "))
    inp.append(temp)
print("Second | Packet Received | Packet Sent | Packet Left | Dropped")
print("--------------------------------------------------------------")
for i in range(nsec):
    count+=inp[i]
    if count>cap:
        drop=count-cap
        count=cap
    print(str(i+1)+"     "+str(inp[i]),end="     ")
    mini=min(count,process)
    print(mini,end="     ")
    count-=mini
    print(str(count)+"     "+str(drop))
    drop=0

while count>0:
    if count>cap:
        drop=count-cap
        count=cap
    print(str(i+2)+"     "+str(inp[i]),end="     ")
    mini=min(count,process)
    print(mini,end="     ")
    count-=mini
    print(str(count)+"     "+str(drop))
    drop=0
    i+=1