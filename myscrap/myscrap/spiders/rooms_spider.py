import scrapy
from scrapy.http import HtmlResponse


class RoomsSpider(scrapy.Spider):
    name = "rooms"
    allowed_domains = ['atira.com']
    start_urls = [
        'https://atira.com/locations/',
    ]

    def parse(self, response):
        locations = response.css('a.location::attr(href)').getall()
        for location in locations:
            yield response.follow(location, callback=self.parse_location)

    def parse_location(self, response):

        rooms = response.css(
            'div.location__rooms--feed a::attr(href)').getall()
        for room in rooms:
            yield response.follow(room, callback=self.parse_room)

    def parse_room(self, response):

        price = response.css('span.room__sidebar--rate-base::text').get()
        capacity_of_persons = response.css(
            'div.room__sidebar--icons ul  li::text').get()
        room_name = response.css('h1.room__title::text').get()
        building_name = response.css('h5.room__location--title::text').get()
        features = self.find_features(response)
        address = response.css('div.address span::text').getall()
        location = ""
        for item in address:
            location += item
        city = self.find_city(location)
        yield {
            'price': float(price),
            'capacity_of_persons': int(capacity_of_persons),
            'features': features,
            'room_name': room_name,
            'building_name': building_name,
            'location': location,
            'url': response.url,
            'city': city,
        }

    def find_features(self, response):

        room_features = response.css('div.room__features').getall()
        features_room = []
        features_apartment = []
        isroom = 1
        for room_features_obj in room_features:
            room_features_response = HtmlResponse(
                url=room_features_obj, body=room_features_obj, encoding='utf-8')
            room__feature = room_features_response.css(
                'div.room__feature').getall()
            for room_feature_obj in room__feature:
                room_feature_response = HtmlResponse(
                    url=room_feature_obj, body=room_feature_obj, encoding='utf-8')
                strong = room_feature_response.css('p strong::text').get()
                paragraph = room_feature_response.css('p::text').get()
                line = ""
                if strong:
                    line = strong
                if paragraph:
                    line = line + paragraph
                if isroom and line:
                    features_room.append(line)
                elif line:
                    features_apartment.append(line)
            isroom = 0
        features = {'features_room': features_room,
                    'features_shared_apartment': features_apartment}
        return features

    def find_city(self, location):

        wordlist = location.split()
        index = 0
        for i in range(len(wordlist)):
            word = wordlist[i]
            if word.isupper():
                break
            else:
                index = i
        city = wordlist[index]
        return city
