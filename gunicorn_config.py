import multiprocessing

bind = "143.244.134.2:8013"  # Replace with your desired IP and port
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2
timeout = 60
