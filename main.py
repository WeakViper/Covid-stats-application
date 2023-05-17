from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.snackbar import Snackbar
import requests
import pickle


class World(FloatLayout):
    colo = ObjectProperty(None)

    f = open('mode.dat', 'rb')
    try:
        de = pickle.load(f)
        colo = de['t']

    except EOFError:

        f.close()

    b_url = 'https://disease.sh/v3/covid-19/all'
    response = requests.get(url=b_url).json()
    case = '{:,}'.format(response['cases'])
    caset = '{:,}'.format(response['todayCases'])
    death = '{:,}'.format(response['deaths'])
    deatht = '{:,}'.format(response['todayDeaths'])
    recover = '{:,}'.format(response['recovered'])
    recovert = '{:,}'.format(response['todayRecovered'])
    active = '{:,}'.format(response['active'])
    critical = '{:,}'.format(response['critical'])
    tests = '{:,}'.format(response['tests'])


class Live(FloatLayout):
    colo = ObjectProperty(None)

    f = open('mode.dat', 'rb')
    try:
        de = pickle.load(f)
        colo = de['t']

    except EOFError:

        f.close()

    j = requests.get("https://geolocation-db.com/json/").json()
    countr = j['country_name'].lower().capitalize()
    l1= countr.split()
    country = "%20".join(l1)


    a_url = 'https://disease.sh/v3/covid-19/countries/{}?yesterday='+country
    response = requests.get(url=a_url.format(country)).json()

    place = countr.upper()
    cases = '{:,}'.format(response['cases'])
    deaths = '{:,}'.format(response['deaths'])
    recovered = '{:,}'.format(response['recovered'])
    active = '{:,}'.format(response['active'])
    todayr = '{:,}'.format(response['todayRecovered'])
    todayc = '{:,}'.format(response['todayCases'])
    todayd = '{:,}'.format(response['todayDeaths'])
    tests = '{:,}'.format(response['tests'])
    critical = '{:,}'.format(response['critical'])


class Search(FloatLayout):
    colo = ObjectProperty(None)
    so = ObjectProperty(None)

    f = open('mode.dat', 'rb')
    try:
        de = pickle.load(f)
        colo = de['t']
        so = de['s']

    except EOFError:

        f.close()

    searchs = ObjectProperty(None)
    place = StringProperty()
    cases = StringProperty()
    deaths = StringProperty()
    recovered = StringProperty()
    active = StringProperty()
    todayc = StringProperty()
    todayd = StringProperty()
    todayr = StringProperty()
    critical = StringProperty()
    tests = StringProperty()
    country = StringProperty()

    def search(self):

        try:
            search = self.searchs.text.lower().capitalize()
            l1 = search.split()
            country = "%20".join(l1)

            a_url = 'https://disease.sh/v3/covid-19/countries/{}?yesterday=' + country
            response = requests.get(url=a_url.format(country)).json()
            self.place = self.searchs.text.upper()
            self.cases = '{:,}'.format(response['cases'])
            self.deaths = '{:,}'.format(response['deaths'])
            self.recovered = '{:,}'.format(response['recovered'])
            self.todayr = '{:,}'.format(response['todayRecovered'])
            self.todayc = '{:,}'.format(response['todayCases'])
            self.todayd = '{:,}'.format(response['todayDeaths'])
            self.active = '{:,}'.format(response['active'])
            self.critical = '{:,}'.format(response['critical'])
            self.tests = '{:,}'.format(response['tests'])

        except:

            Snackbar(text='Invalid country name, Please try again.').open()
            self.place = ''
            self.cases = str(0)
            self.deaths = str(0)
            self.recovered = str(0)
            self.active = str(0)
            self.todayc = str(0)
            self.todayd = str(0)
            self.todayr = str(0)
            self.critical = str(0)
            self.tests = str(0)


class Options(FloatLayout):
    colo = ObjectProperty(None)

    f = open('mode.dat', 'rb')
    try:
        de = pickle.load(f)
        colo = de['t']

    except EOFError:

        f.close()

    def dark(self):
        f = open('mode.dat', 'wb')
        ca = {'t': (1, 1, 1, 1), 'p': 'Dark', 's': (0, 0, 0, 0)}
        pickle.dump(ca, f)
        f.close()
        exit()

    def light(self):

        f = open('mode.dat', 'wb')
        ca = {'t': (0, 0, 0, 1), 'p': 'Light', 's': (1, 1, 1, 1)}
        pickle.dump(ca, f)
        f.close()
        exit()

class MainApp(MDApp):
    f = open('mode.dat', 'rb')
    try:
        de = pickle.load(f)
        templa = de['p']

    except EOFError:

        f.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = self.templa
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'


MainApp().run()
