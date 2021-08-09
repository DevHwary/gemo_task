from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
import requests


@api_view(['GET'])
def list_top_100_language(request):
    """
    List programming languages, num_of_repos, and URLs of the top 100 trending repository on githup in last 30 days
    """
    try :
        today = datetime.now()
        thirty_days_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")

        # Repositories Search API : https://docs.github.com/en/rest/reference/search#search-repositories
        url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(thirty_days_ago)

        response = requests.get(url)
        trending_repositories = response.json()['items']

        list_languages = {}
        NO_OF_REPOS = "Number of repos"
        LIST_OF_REPOS = "List of repos"
        URL = "url"
        HTML_URL = "html_url"

        for repo in trending_repositories:
            language = repo['language']
            # From inside the list_languages DICT. Get or create the current repository's language data.
            prevEntry = list_languages.setdefault(language,
                                                      {NO_OF_REPOS: 0,
                                                       LIST_OF_REPOS: []})

            list_languages[language][NO_OF_REPOS] = prevEntry[NO_OF_REPOS] + 1
            list_languages[language][LIST_OF_REPOS].append({repo[URL], repo[HTML_URL]})
        return Response(list_languages, status=status.HTTP_200_OK)

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
