import json
import matplotlib.pyplot as plt
import numpy


def list_cities(data):

    city_list = []
    for x in data:
        if x['city'] not in city_list:
            city_list.append(x['city'])
    return city_list


def list_capacity_of_persons(data):

    capacity = []
    for x in data:
        if x['capacity_of_persons'] not in capacity:
            capacity.append(x['capacity_of_persons'])
    return capacity


def average_price_of_city_capacity_of_persons(data, city, capacity):

    total = 0
    count = 0
    avg = 0
    city_capacity_price = {}
    for x in data:
        if x['capacity_of_persons'] == capacity and x['city'] == city:
            total = total + x['price']
            count = count + 1
    if count != 0:
        avg = total / count
        city_capacity_price['city'] = city
        city_capacity_price['capacity'] = capacity
        city_capacity_price['avg'] = avg
    return city_capacity_price


def get_city_capacity_price(city_capacity_price_list, city, capacity):

    city_capacity_price = {}
    for item in city_capacity_price_list:
        if item['city'] == city and item['capacity'] == capacity:
            city_capacity_price = item
            break
    return city_capacity_price


def plot(city_capacity_price_list, capacity_list, city_list):

    for city in city_list:
        ylist = []
        for capacity in capacity_list:
            city_capacity_price = get_city_capacity_price(
                city_capacity_price_list, city, capacity)
            if city_capacity_price:
                ylist.append(city_capacity_price['avg'])
            else:
                ylist.append(0)
        plt.plot(capacity_list, ylist, color=numpy.random.rand(3,), label=city)
    plt.ylabel('Average price')
    plt.xlabel('Capacity of persons')
    plt.title('Average price of rooms in cities')
    plt.legend()
    plt.show()


with open('rooms.json') as f:
    data = json.load(f)
city_list = list_cities(data)
city_list = sorted(city_list)
capacity_list = list_capacity_of_persons(data)
capacity_list = sorted(capacity_list)
city_capacity_price_list = []
for city in city_list:
    for capacity in capacity_list:
        city_capacity_price = average_price_of_city_capacity_of_persons(
            data, city, capacity)
        if city_capacity_price:
            city_capacity_price_list.append(city_capacity_price)
            print(city, " ", capacity, " person capacity average price is " +
                  "{:.2f}".format(city_capacity_price['avg']))
    print('\n\n')
plot(city_capacity_price_list, capacity_list, city_list)
