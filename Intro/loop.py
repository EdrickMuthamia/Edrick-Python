# for ,while , do_while

to_loop=True
i=0

# while (<condition>):

while to_loop:
   if i>10:
      to_loop=False
   print("i is",i)
   i=i+1 

# WEB->JS
k=0
while k<10:
   print("k is",k)
   k=k+1

#for(let i=0;i<10;i++)

# starting 2 to 10
for i in range(2,10):
   print("For loop is is",i)

#from 10 to 
for i in range(10,2,-1):
   print("For loop is ",i)


   for i in range (0,1000,2):
    print("All even numbers",i)