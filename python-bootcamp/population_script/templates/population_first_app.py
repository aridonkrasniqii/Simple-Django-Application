import os
import django
import random
from population_app.models import AccessRecord, WebPage, Topic
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'population_app.settings')

django.setup()

## FAKE POPULATION SCRIPT

faker = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data
        fake_url = faker.url()
        fake_date = faker.date()
        fake_name = faker.company()

        # Create the new webpage entry

        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        # pass the entire object as a foreing key
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populationg script !')
    populate(20)
    print('Populating complete !')
