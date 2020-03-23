# rss_reader
## Django Developer assignment
## Task
##### Your task is to create a Django application that is a feeds reader. The app can read feed from multiple sources and store them to database. Sample feeds http://www.feedforall.com/sample-feeds.htm.
##### Requirements: As a developer
- to run a command which help me to setup database easily with one run:

    ##### Activate your virtual environment, then:
    #####/rss_reader$ `pip install -r requirements.txt `
    #####/rss_reader$ `python manage.py migrate`

- to run a command which accepts the feed urls (separated by comma) as argument to grab items from given urls. Duplicate items are accepted.

   #####/rss_reader$ `python manage.py rss --scrawl https://www.feedforall.com/sample.xml,https://www.feedforall.com/sample-feed.xml `

- to see output of the command not only in shell but also in pre-defined log file. The log file should be defined as a parameter of the application.

   #####/rss_reader/settings.py `LOG_URL = os.getenv('DJANGO_LOG_FILE', 'info.log')`

##### Requirements: As a user

    Activate your virtual environment, then:
    /rss_reader$ python manage.py runserver
- to see the list of items which were grabbed by running the command line above, via web-based. I also should see the pagination if there are more than one page. The page size is a configurable value.

   #####/rss_reader/settings.py `PAGINATION_ADMIN_DASHBOARD = os.getenv('PAGINATION_ADMIN_DASHBOARD', 30)`

- to filter items by category name on list of items: OK

   #####visit `http://localhost:8000/rss/rss/`
  
- to create new item manually via a form: OK

   #####visit `http://localhost:8000/rss/rss/add/`

- to update/delete an item: OK

   #####visit `http://localhost:8000/rss/rss/{id}/change/`
