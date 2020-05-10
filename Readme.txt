Did some research on avaiable liabraries for scrapping
Used scrapy for scrapping 
documentation used https://docs.scrapy.org/en/latest/intro/tutorial.html

To run web crawler:
	open windows shell
	install python and libraries scrapy, matplotlib
	move to root directory of my scrapy project "myscrap"
	delete existing jason file to avoid redundancy of data in jason
	run command "scrapy crawl rooms -o rooms.json" to run crawler
	it will create rooms.json file in "myscrap" directory
	my code is at path "myscrap/myscrap/spiders/rooms_spider.py"
	
To run analysis
	copy rooms.json to directory analysis
	open windows shell
	activate venv
	move to directory analysis
	run command "python.exe main.py"
	it will show details on console and a graph
	