def compute(n):
    import socket
    return socket.gethostname(), sum(n)


if __name__ == '__main__':
    import dispy
    import random
    cluster = dispy.JobCluster(compute, nodes=["192.168.1.114", "192.168.1.141"])
    jobs = []

    data = [random.randint(1, 1000) for _ in range(1000000)]

    jobs_count = 10
    chunk_size = int(len(data) / jobs_count)

    for i in range(jobs_count):
        job = cluster.submit(data[i*chunk_size:i*chunk_size + chunk_size])
        job.id = i
        jobs.append(job)

    total = 0
    for job in jobs:
        # waits for job to finish and returns results
        host, sub_sum = job()
        print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, sub_sum))
        total += sub_sum
    cluster.print_status()
    cluster.close()
    print(total)

