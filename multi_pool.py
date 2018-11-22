#coding:utf-8

__author__ = 'kzk'


"多线程和多进程"



"""
多任务的目的是为了压榨CPU的执行效率，对于计算密集型任务十分适用。

多线程：

Python的标准库提供了两个模块：_thread和threading.
_thread是低级模块，一般不用了
threading是高级模块，对_thread进行了封装。

threading.current_thread()   返回的是当前线程的实例(object)
threading.active_count()     返回alive线程数量
mydata = threading.local()   每个线程不同，可以有特定的值
mydata.x = 1


flag = threading.Event()  返回一个事件
flag.is_set()/  set()  /clear()

threading.active_count()  列举出存活线程个数
threading.enumerate()     列举出当前的存活线程（包括执行，阻塞），不包括结束的

在多线程中，由于GIL，全局解释锁，每次只能允许一个线程执行。因此，为了使用CPU资源，
可以使用多进程，multiprocessing 模块。而对于IO密集型任务，多线程仍然有较好的表现。

单进程的异步编程模型称为协程
"""









import time, threading
import os


def Threadcount():
    print('%d Process %s Thread is running...' %( os.getpid(), threading.current_thread().name) )  
    print("Start Count\n")

    
    for i in xrange(1,10):
        print ("i = %d" % i )
        time.sleep(1)
    print("End Count")
    
    #while True:
    #    print('%d Pro- %s Th' %( os.getpid(), threading.current_thread().name) )  
     
            

def ThreadingTest():
    print('%d Process %s Thread is running...' %( os.getpid(), threading.current_thread().name) )  
    th = threading.Thread(target = Threadcount, name = "Th-1")
    th.start()
    th.join()
    print('%d Process %s Thread quits...\n' %( os.getpid(), threading.current_thread().name) )  




def DaemonTh():
    print("Enter Daemon")

    while True:
        time.sleep(2)
        print(" Daemon Thread : %d live" % threading.active_count())
        for th in threading.enumerate():
            print( th.name)


def DaemonTest():
    DaeTh = threading.Thread(target = DaemonTh, name ='MyDeamon')
    DaeTh.setDaemon(True)

    CTh = threading.Thread(target = Threadcount, name ='MyThreadCount')
    DaeTh.start()
    CTh.start()
    for x in xrange(1,4):
        time.sleep(1)
    #CTh.join()








def Processcount(name):
    print('%s Process %d------->Start ' % (name, os.getpid() ))
    ThreadingTest()



def ProcessTest():
    print('Process %s is running' % os.getpid() )
    pro1 = Process(target = Processcount, args= ('sub1',) )
    pro2 = Process(target = Processcount, args= ('sub2',) )
    pro1.start()
    pro2.start()
    pro1.join()
    pro2.join()



"""
多进程：

from multiprocessing import Pool, Process
Process是生成进程
Process follows the API of threading.Thread，所以和上面的用法一样。
Process(group=None, target=None, name=None, args=(), kwargs={})



Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])

apply(func[, args[, kwds]]) #执行完才解锁
apply_async(func[, args[, kwds[, callback]]])  #并行，执行完可以通过callback返回
map(func, iterable[, chunksize])  #iterable 参数，阻塞，只有结束才能返回结果，不并行；
map_async(func, iterable[, chunksize[, callback]]) ##iterable 参数，可并行


"""

from multiprocessing import Pool, Process
import time

def Foo(i):
    time.sleep(2)
    print('___time---',time.ctime())
    return i+100

def Bar(arg):
    print('----exec done:',arg,time.ctime())

def ProcessTest():
    pool = Pool(3) #进程池中的同时执行的进程数，最大最好设置为物理机上CPU的核心数。

    for i in range(5):
        pool.apply_async(func=Foo,args=(i,),callback=Bar) 
        #线程池中的同时执行的进程数为3，当一个进程执行完毕后，如果还有新进程等待执行，则会将其添加进去
        # pool.apply(func=Foo,args=(i,)
    pool.close()
    pool.join()
    #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print('end')
    #为什么先执行的bar内容，再执行的是Foo的剩余代码？
    #命令行中，顺序是正确的。
    #应该是先执行3个，然后最后2个执行。


if __name__ == '__main__':
    #freeze_support()
    ProcessTest()
    

    """
    #ThreadingTest()
    #ProcessTest()
    """
    """
    th = threading.Thread(target = DaemonTest, name ="main_created")
    th.start()
    th.join()
    print("main-finish")
    """
