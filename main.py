try:
    import requests
    import json
    from bs4 import BeautifulSoup
    import random
except ModuleNotFoundError:
    print('Modules not found. Please run pip install -r requirements.txt to install the required modules.')
    exit()


def movie_info(parsed):
    title = parsed['Title']
    genre = parsed['Genre']
    ratings = parsed['Ratings'][0]['Value']
    MPAA_rating = parsed['Rated']
    year = parsed['Year']
    director = parsed['Director']
    cast = parsed['Actors']
    print('Recommended movie: ')
    print(f'Title: {title}({year})')
    print(f'Genre: {genre}')
    print(f'Rating: {ratings} ({MPAA_rating})')
    print(f'Director: {director}')
    print(f'Cast: {cast}')
    return ''


def api_movie_data(selected_movie):
    movie_url = f'http://www.omdbapi.com/?apikey=[YOUR API KEY]&t={selected_movie}&type=movie'
    res = requests.get(movie_url)
    data = res.text
    parsed = dict(json.loads(data))
    return parsed


def imdb_top_movie_list():
    movie_title_list = []
    movie_list_url = 'https://www.imdb.com/list/ls068082370/'
    res_list = requests.get(movie_list_url)
    soup = BeautifulSoup(res_list.text, 'html.parser')
    movie_list = soup.find_all('h3')
    for i in movie_list:
        try:
            movie_title_list.append(i.find('a').text)
        except:
            break
    return movie_title_list


def random_movie_from_imdb(imdb_top_movie_list):
    selected_movie = random.choice(imdb_top_movie_list())
    return selected_movie


if __name__ == '__main__':
    movie_info(api_movie_data(random_movie_from_imdb(imdb_top_movie_list)))
