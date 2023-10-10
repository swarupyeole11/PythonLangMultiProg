import threading
import time

### VVVVV Intresting fact 
# THere are two types of speed there is server spped and and internet speed Now suppose you have to download 4 files your internet speed is 2gbps but the sercer sppeed is 500mbps then your download speed will limit to 500mbps only 
# In such cases using multthrading to paralley run 4 servers helps us use out whole internet bandwidth HENCE FOR SUCH WE NEED MULTITHREADING

def func(*args) :
#   here imagine sleep as a network call to api which will take some time also I have used args just to check it's fuctionaliyt and how it works
   time.sleep(args[0])
   print(f" THe function has run for {args[0]} seconds ")


def multithredingdemo():

    time_intital = time.perf_counter()
    func(4)
    func(2)
    func(1)
    print("Time taken by normal process  wihtout multithreading : \n",time.perf_counter()-time_intital)

    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func,args=[1])

    time_intital = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    print("This time indicates that the process has started exucting asynchronoysly and running in the background but has not complted yet : \n",time.perf_counter()-time_intital)
    
    # The join statemnt makes us wait for the thread execution to completer
    t1.join()
    t2.join()
    t3.join()
    print("This time indicates the time taken when we waited for the process to complete using join : \n",time.perf_counter()-time_intital)


multithredingdemo()