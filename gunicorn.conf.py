from multiprocessing import cpu_count


def max_workers():
    return cpu_count() * 2 + 1


def max_threads():
    return cpu_count() * 2


max_requests = 100000
workers = max_workers()
threads = max_threads()
worker_class = 'gthread'
worker_tmp_dir = '/dev/shm'
bind = '0.0.0.0:8001'

keepalive = 75
