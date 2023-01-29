# Clothing Search Engine App
In this project, I built a clothes search engine that includes Crawler, Backend Side ( Api ), and Frontend Side.

First, we get Banimode.com site information through a crawler and store this information in a MongoDB database.
Then, by flask framework, I write an API that sends the information in the MongoDB database to the Frontend section.

Finally, we run all the parts with Docker and re-execute the crawler part at certain times by Celery.
