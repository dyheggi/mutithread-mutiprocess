import spider
import threading
import time


def single_thread():
    print("single_thread begin")
    for url in spider.urls:
        spider.craw(url)
    print("single_thread end")


def multi_thread():
    threads = []
    print("multi_thread begin")
    for url in spider.urls:
        threads.append(
            threading.Thread(target=spider.craw, args=(url,))
        )
    print("multi_thread end")

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


start = time.time()
single_thread()
end = time.time()
print("single_thread cost:", end - start, "seconds")

start = time.time()
multi_thread()
end = time.time()
print("multi_thread cost:", end - start, "seconds")
