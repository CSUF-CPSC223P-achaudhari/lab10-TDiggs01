import json


def bot_clerk(lst=[]):
    cart_list = []
    thread_lock = []

    robo1 = bot_fetcher(lst)
    robo2 = bot_fetcher(lst)
    robo3 = bot_fetcher(lst)

    json_file = open('inventory.dat', 'r')
    line = json.load(json_file)
    json_file.close()
    #for i in line:
     #   print(i)
    return lst


def bot_fetcher(item=[], thread_lock=0):
    robo_fetch = [item for i in range(3)]

    for key, val in enumerate(item):
        robo_fetch[key % 3].append(item)
    return robo_fetch

def main():
  pass


if __name__ == "__main__":
    main()
