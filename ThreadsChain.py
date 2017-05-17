import threading


thread_max_num = 50
threads = []

def create_new_thread(thread_count):
    global threads
    print('Hello from', threading.currentThread().getName(), '!')
    if thread_count < thread_max_num:
        thread_count += 1
        t = threading.Thread(target=create_new_thread, args=(thread_count,))
        threads.append(t)
        myName = "Thread " + str(thread_count)
        t.setName(myName)
        t.start()
    return

 
def main():
    thread_count = 1
    
    t = threading.Thread(target=create_new_thread, args=(thread_count,))
    threads.append(t)
    myName = "Thread " + str(thread_count)
    t.setName(myName)
    t.start()
    
    for thread in threads:
        thread.join()
    return

if __name__ == '__main__':
    main()


