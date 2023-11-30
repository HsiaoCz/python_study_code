# python的多线程编程
# 操作线程能够调动的最小 线程
# 对于io操作来说，多线程和多进程性能差别不大
# 通过thread类实例化

from collections.abc import Callable, Iterable, Mapping
import threading
import time
from typing import Any


def get_datail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


# 通过继承thread类来实现多线程
class GetDetailHTML(threading.Thread):
    def __init__(
        self,
        group: None = None,
        target: Callable[..., object] | None = None,
        name: str | None = None,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] | None = None,
        *,
        daemon: bool | None = None
    ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailURL(threading.Thread):
    def __init__(
        self,
        group: None = None,
        target: Callable[..., object] | None = None,
        name: str | None = None,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] | None = None,
        *,
        daemon: bool | None = None
    ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


if __name__ == "__main__":
    thread1 = threading.Thread(target=get_datail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # 当主线程退出的时候，子线程kill
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()

    # 等待线程执行完成
    thread1.join()
    thread2.join()
    # 当主线程退出的时候，子线程kill
    print("last time:{}".format(time.time() - start_time))

    thread3 = GetDetailHTML("get_detail_html")
    thread4 = GetDetailURL("get_detail_url")
    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()
