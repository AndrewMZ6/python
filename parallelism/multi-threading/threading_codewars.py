# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
# solving codewars kata using threads
import threading
import time
from faker import Faker

ipv4_gen = Faker()
customers = [ipv4_gen.ipv4() for _ in range(20)]


# customers = [2,2,3,3,4,4]
n = 3
index = 0


def handle():
    name = threading.currentThread().getName()
    global customers
    thread_list = []
    global index
    iteration_number = 0
    while index < len(customers):
        print(f"[{name}]-> iteration_number: {iteration_number}")
        print(f"[{name}]-> index supposed to append: {index}")
        t = customers[index]
        print(f"[{name}]-> index of appended element: {customers.index(t)}")
        thread_list.append(t)
        print(f"[{name}]-> current thread_list: {thread_list}\n")
        index += 1
        iteration_number += 1
        time.sleep(1)
    print(f"[{name}]-> final thread_list: {thread_list}")
    return thread_list


def queue_time(customers, n):
    name_gen = Faker()
    thread_names = [name_gen.word() for _ in range(n)]
    threads = [
        threading.Thread(target=handle, name=uwu.capitalize()) for uwu in thread_names
    ]
    for thread in threads:
        thread.start()
        time.sleep(0.25)

    for thread in threads:
        thread.join()


queue_time(customers, n)

# OUTPUT:
# [Talk]-> iteration_number: 0
# [Talk]-> index supposed to append: 0
# [Talk]-> index of appended element: 0
# [Talk]-> current thread_list: ['42.233.220.176']

# [Face]-> iteration_number: 0
# [Face]-> index supposed to append: 1
# [Face]-> index of appended element: 1
# [Face]-> current thread_list: ['173.116.24.146']

# [High]-> iteration_number: 0
# [High]-> index supposed to append: 2
# [High]-> index of appended element: 2
# [High]-> current thread_list: ['214.176.223.92']

# [High]-> iteration_number: 1
# [Talk]-> iteration_number: 1[Face]-> iteration_number: 1[High]-> index supposed to append: 3
# [High]-> index of appended element: 3

# [Talk]-> index supposed to append: 3

# [Face]-> index supposed to append: 3
# [High]-> current thread_list: ['214.176.223.92', '162.66.199.175']
# [Face]-> index of appended element: 3
# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175']

# [Talk]-> index of appended element: 3

# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175']

# [Talk]-> iteration_number: 2
# [Talk]-> index supposed to append: 6
# [Talk]-> index of appended element: 6[Face]-> iteration_number: 2
# [Face]-> index supposed to append: 6[High]-> iteration_number: 2

# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5']


# [High]-> index supposed to append: 6
# [Face]-> index of appended element: 6[High]-> index of appended element: 7
# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5']


# [High]-> current thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90']

# [High]-> iteration_number: 3
# [High]-> index supposed to append: 9[Face]-> iteration_number: 3[Talk]-> iteration_number: 3
# [High]-> index of appended element: 9
# [High]-> current thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90', '153.195.106.148']


# [Talk]-> index supposed to append: 9
# [Talk]-> index of appended element: 9
# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5', '153.195.106.148']


# [Face]-> index supposed to append: 10
# [Face]-> index of appended element: 11
# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5', '119.128.157.164']

# [Talk]-> iteration_number: 4[High]-> iteration_number: 4

# [High]-> index supposed to append: 12
# [Talk]-> index supposed to append: 12[Face]-> iteration_number: 4[High]-> index of appended element: 12


# [Face]-> index supposed to append: 12
# [Face]-> index of appended element: 12
# [Talk]-> index of appended element: 12[High]-> current thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90', '153.195.106.148', '98.233.229.201']


# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5', '119.128.157.164', '98.233.229.201']

# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5', '153.195.106.148', '98.233.229.201']

# [Face]-> iteration_number: 5[Talk]-> iteration_number: 5[High]-> iteration_number: 5

# [Talk]-> index supposed to append: 15
# [Face]-> index supposed to append: 15
# [Talk]-> index of appended element: 15
# [Face]-> index of appended element: 15
# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5', '153.195.106.148', '98.233.229.201', '85.62.67.179']

# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5', '119.128.157.164', '98.233.229.201', '85.62.67.179']


# [High]-> index supposed to append: 16
# [High]-> index of appended element: 17
# [High]-> current thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90', '153.195.106.148', '98.233.229.201', '61.74.43.78']

# [High]-> iteration_number: 6[Talk]-> iteration_number: 6

# [High]-> index supposed to append: 18[Face]-> iteration_number: 6
# [High]-> index of appended element: 18

# [Talk]-> index supposed to append: 18
# [Talk]-> index of appended element: 18
# [Talk]-> current thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5', '153.195.106.148', '98.233.229.201', '85.62.67.179', '82.43.19.198']
# [Face]-> index supposed to append: 18

# [High]-> current thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90', '153.195.106.148', '98.233.229.201', '61.74.43.78', '82.43.19.198']

# [Face]-> index of appended element: 19
# [Face]-> current thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5', '119.128.157.164', '98.233.229.201', '85.62.67.179', '149.255.148.251']

# [Face]-> final thread_list: ['173.116.24.146', '162.66.199.175', '10.88.228.5', '119.128.157.164', '98.233.229.201', '85.62.67.179', '149.255.148.251'][High]-> final thread_list: ['214.176.223.92', '162.66.199.175', '66.215.217.90', '153.195.106.148', '98.233.229.201', '61.74.43.78', '82.43.19.198']
# [Talk]-> final thread_list: ['42.233.220.176', '162.66.199.175', '10.88.228.5', '153.195.106.148', '98.233.229.201', '85.62.67.179', '82.43.19.198']

# [Finished in 7.7s]


######################################################################
# if uncomment the time.sleep(0.25) in line 39 we get perfect result:
# [Word]-> iteration_number: 0
# [Word]-> index supposed to append: 0
# [Word]-> index of appended element: 0
# [Word]-> current thread_list: ['64.252.16.89']

# [Kind]-> iteration_number: 0
# [Kind]-> index supposed to append: 1
# [Kind]-> index of appended element: 1
# [Kind]-> current thread_list: ['198.230.150.63']

# [Test]-> iteration_number: 0
# [Test]-> index supposed to append: 2
# [Test]-> index of appended element: 2
# [Test]-> current thread_list: ['113.192.217.67']

# [Word]-> iteration_number: 1
# [Word]-> index supposed to append: 3
# [Word]-> index of appended element: 3
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204']

# [Kind]-> iteration_number: 1
# [Kind]-> index supposed to append: 4
# [Kind]-> index of appended element: 4
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181']

# [Test]-> iteration_number: 1
# [Test]-> index supposed to append: 5
# [Test]-> index of appended element: 5
# [Test]-> current thread_list: ['113.192.217.67', '115.210.29.54']

# [Word]-> iteration_number: 2
# [Word]-> index supposed to append: 6
# [Word]-> index of appended element: 6
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33']

# [Kind]-> iteration_number: 2
# [Kind]-> index supposed to append: 7
# [Kind]-> index of appended element: 7
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119']

# [Test]-> iteration_number: 2
# [Test]-> index supposed to append: 8
# [Test]-> index of appended element: 8
# [Test]-> current thread_list: ['113.192.217.67', '115.210.29.54', '173.88.96.172']

# [Word]-> iteration_number: 3
# [Word]-> index supposed to append: 9
# [Word]-> index of appended element: 9
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33', '7.30.61.235']

# [Kind]-> iteration_number: 3
# [Kind]-> index supposed to append: 10
# [Kind]-> index of appended element: 10
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119', '148.234.248.179']

# [Test]-> iteration_number: 3
# [Test]-> index supposed to append: 11
# [Test]-> index of appended element: 11
# [Test]-> current thread_list: ['113.192.217.67', '115.210.29.54', '173.88.96.172', '87.80.104.224']

# [Word]-> iteration_number: 4
# [Word]-> index supposed to append: 12
# [Word]-> index of appended element: 12
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33', '7.30.61.235', '12.171.112.58']

# [Kind]-> iteration_number: 4
# [Kind]-> index supposed to append: 13
# [Kind]-> index of appended element: 13
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119', '148.234.248.179', '206.143.202.184']

# [Test]-> iteration_number: 4
# [Test]-> index supposed to append: 14
# [Test]-> index of appended element: 14
# [Test]-> current thread_list: ['113.192.217.67', '115.210.29.54', '173.88.96.172', '87.80.104.224', '178.22.207.134']

# [Word]-> iteration_number: 5
# [Word]-> index supposed to append: 15
# [Word]-> index of appended element: 15
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33', '7.30.61.235', '12.171.112.58', '211.54.73.99']

# [Kind]-> iteration_number: 5
# [Kind]-> index supposed to append: 16
# [Kind]-> index of appended element: 16
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119', '148.234.248.179', '206.143.202.184', '180.219.87.81']

# [Test]-> iteration_number: 5
# [Test]-> index supposed to append: 17
# [Test]-> index of appended element: 17
# [Test]-> current thread_list: ['113.192.217.67', '115.210.29.54', '173.88.96.172', '87.80.104.224', '178.22.207.134', '153.219.82.178']

# [Word]-> iteration_number: 6
# [Word]-> index supposed to append: 18
# [Word]-> index of appended element: 18
# [Word]-> current thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33', '7.30.61.235', '12.171.112.58', '211.54.73.99', '176.216.186.27']

# [Kind]-> iteration_number: 6
# [Kind]-> index supposed to append: 19
# [Kind]-> index of appended element: 19
# [Kind]-> current thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119', '148.234.248.179', '206.143.202.184', '180.219.87.81', '112.2.78.68']

# [Test]-> final thread_list: ['113.192.217.67', '115.210.29.54', '173.88.96.172', '87.80.104.224', '178.22.207.134', '153.219.82.178']
# [Word]-> final thread_list: ['64.252.16.89', '216.92.247.204', '204.58.103.33', '7.30.61.235', '12.171.112.58', '211.54.73.99', '176.216.186.27']
# [Kind]-> final thread_list: ['198.230.150.63', '58.188.215.181', '221.24.119.119', '148.234.248.179', '206.143.202.184', '180.219.87.81', '112.2.78.68']
# [Finished in 7.9s]

####################################################################################
# number of threads n = 20, delay = 0.1
# [Let]-> iteration_number: 0
# [Let]-> index supposed to append: 0
# [Let]-> index of appended element: 0
# [Let]-> current thread_list: ['13.150.188.208']

# [Job]-> iteration_number: 0
# [Job]-> index supposed to append: 1
# [Job]-> index of appended element: 1
# [Job]-> current thread_list: ['126.83.138.132']

# [Morning]-> iteration_number: 0
# [Morning]-> index supposed to append: 2
# [Morning]-> index of appended element: 2
# [Morning]-> current thread_list: ['132.188.252.218']

# [Reality]-> iteration_number: 0
# [Reality]-> index supposed to append: 3
# [Reality]-> index of appended element: 3
# [Reality]-> current thread_list: ['8.165.73.136']

# [Father]-> iteration_number: 0
# [Father]-> index supposed to append: 4
# [Father]-> index of appended element: 4
# [Father]-> current thread_list: ['38.77.212.59']

# [Certain]-> iteration_number: 0
# [Certain]-> index supposed to append: 5
# [Certain]-> index of appended element: 5
# [Certain]-> current thread_list: ['3.102.55.152']

# [Law]-> iteration_number: 0
# [Law]-> index supposed to append: 6
# [Law]-> index of appended element: 6
# [Law]-> current thread_list: ['185.242.223.246']

# [Story]-> iteration_number: 0
# [Story]-> index supposed to append: 7
# [Story]-> index of appended element: 7
# [Story]-> current thread_list: ['35.114.231.249']

# [Say]-> iteration_number: 0
# [Say]-> index supposed to append: 8
# [Say]-> index of appended element: 8
# [Say]-> current thread_list: ['48.80.250.252']

# [Road]-> iteration_number: 0
# [Road]-> index supposed to append: 9
# [Road]-> index of appended element: 9
# [Road]-> current thread_list: ['84.201.28.71']

# [Guy]-> iteration_number: 0
# [Guy]-> index supposed to append: 10
# [Guy]-> index of appended element: 10
# [Guy]-> current thread_list: ['12.176.132.51']

# [Leader]-> iteration_number: 0
# [Leader]-> index supposed to append: 11
# [Leader]-> index of appended element: 11
# [Leader]-> current thread_list: ['89.53.160.70']

# [Give]-> iteration_number: 0
# [Give]-> index supposed to append: 12
# [Give]-> index of appended element: 12
# [Give]-> current thread_list: ['120.26.147.199']

# [Over]-> iteration_number: 0
# [Over]-> index supposed to append: 13
# [Over]-> index of appended element: 13
# [Over]-> current thread_list: ['9.250.75.164']

# [Field]-> iteration_number: 0
# [Field]-> index supposed to append: 14
# [Field]-> index of appended element: 14
# [Field]-> current thread_list: ['9.152.106.70']

# [Painting]-> iteration_number: 0
# [Painting]-> index supposed to append: 15
# [Painting]-> index of appended element: 15
# [Painting]-> current thread_list: ['31.235.146.3']

# [Mind]-> iteration_number: 0
# [Mind]-> index supposed to append: 16
# [Mind]-> index of appended element: 16
# [Mind]-> current thread_list: ['199.120.21.192']

# [Yourself]-> iteration_number: 0
# [Yourself]-> index supposed to append: 17
# [Yourself]-> index of appended element: 17
# [Yourself]-> current thread_list: ['121.244.138.157']

# [Similar]-> iteration_number: 0
# [Similar]-> index supposed to append: 18
# [Similar]-> index of appended element: 18
# [Similar]-> current thread_list: ['68.77.244.49']

# [Of]-> iteration_number: 0
# [Of]-> index supposed to append: 19
# [Of]-> index of appended element: 19
# [Of]-> current thread_list: ['116.165.236.19']

# [Let]-> final thread_list: ['13.150.188.208']
# [Job]-> final thread_list: ['126.83.138.132']
# [Morning]-> final thread_list: ['132.188.252.218']
# [Reality]-> final thread_list: ['8.165.73.136']
# [Father]-> final thread_list: ['38.77.212.59']
# [Certain]-> final thread_list: ['3.102.55.152']
# [Law]-> final thread_list: ['185.242.223.246']
# [Story]-> final thread_list: ['35.114.231.249']
# [Say]-> final thread_list: ['48.80.250.252']
# [Road]-> final thread_list: ['84.201.28.71']
# [Guy]-> final thread_list: ['12.176.132.51'][Leader]-> final thread_list: ['89.53.160.70']

# [Give]-> final thread_list: ['120.26.147.199']
# [Over]-> final thread_list: ['9.250.75.164']
# [Field]-> final thread_list: ['9.152.106.70']
# [Painting]-> final thread_list: ['31.235.146.3'][Mind]-> final thread_list: ['199.120.21.192']

# [Yourself]-> final thread_list: ['121.244.138.157']
# [Similar]-> final thread_list: ['68.77.244.49']
# [Of]-> final thread_list: ['116.165.236.19']
# [Finished in 1.9s]
