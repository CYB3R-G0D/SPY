# import modules urllib, thread, lock and queue  
import urllib.request, urllib.error
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_usernames = []

# scan_sites from username
def scan_sites(username):
    global q
    while True:
        sites = q.get()
        url = f"{sites}{username}"
        try:
            conn = urllib.request.urlopen(url)
        # 404 error code, page does not exist
        except urllib.error.HTTPError as e:
            # create text file and save profile pages that dosent exist
            text_file = open(f"{username}""_not_found.txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()
            print("[-] No user found:", f"{sites}")
        # connection reffused to site    
        except urllib.error.URLError as e:
            # create text file error_logs.txt and enter sites that reffused to connect
            text_file = open("error_logs/error_logs.txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()
            # show sites that reffused to connect
            print('[!] Connection reffused to', f"{sites}")
            pass
        else:
            # export found profile page urls to a text file
            text_file = open(f"{username}"".txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()  
            print("[+] User found in", url)
            with list_lock:
                discovered_usernames.append(url)   
        q.task_done()

def main(username, n_threads, sites):
    global q

    for sites in sites:
        q.put(sites)   

    for t in range(n_threads):
        worker = Thread(target=scan_sites, args=(username,))
        worker.daemon = True
        worker.start()


if __name__ == "__main__":
    import argparse
    print("""
 ___ _ __  _   _
/ __| '_ \| | | |
\__ | |_) | |_| |
|___| .__/ \__, |
    |_|    |___/
# Social account scanner by @cyb3r-g0d
    """ )      
    parser = argparse.ArgumentParser(description="An OSINT tool to scan social media accounts by username across social networks")
    parser.add_argument("username", help="username to scan for sites")
    parser.add_argument("-l", "--sitelist", help="File that contains all sites to scan, line by line. Default is sites.txt",
    default="res/sites.txt")
    parser.add_argument("-t", "--num-threads", help="Number of threads to use to scan the username. Default is 10", default=10, type=int)

    args = parser.parse_args()
    username = args.username
    sitelist = args.sitelist
    num_threads = args.num_threads

    main(username=username, n_threads=num_threads, sites=open(sitelist).read().splitlines())
    q.join() 