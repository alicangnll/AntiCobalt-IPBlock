import shodan, os, platform, csv
API_KEY = "SHODAN_API"

class Color():
    @staticmethod
    def red(str):
        return "\033[91m" + str + "\033[0m"
    @staticmethod
    def green(str):
        return "\033[92m" + str + "\033[0m"
    @staticmethod
    def yellow(str):
        return "\033[93m" + str + "\033[0m"
    @staticmethod
    def blue(str):
        return "\033[94m" + str + "\033[0m"

def shodan_cobalt(SHODAN, searchkey):
    try:
        api = shodan.Shodan(SHODAN)
        results = api.search(str(searchkey))
        for result in results['matches']:
            ip = format(result['ip_str'])
            if(platform.system() == "Windows"):
                print(Color.red("Windows are not supporting!"))
            else:
                print(Color.red(str(ip) + " IP adresi engellendi!\n"))
                os.system('iptables -A INPUT -s ' + str(ip) + ' -j DROP')
                os.system('iptables -A OUTPUT -d ' + str(ip) + ' -j DROP')
                data = [str(searchkey), str(ip)]
                with open('ipttable.csv', 'w') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
    except:
        print(Color.red("HARD ERROR"))



while(True):
    arraysearch = ['product:"Cobalt Strike Beacon"', 'product:"Cobalt"']
    for search in arraysearch:
        shodan_cobalt(API_KEY, search)
