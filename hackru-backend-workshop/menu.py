import json
import requests
from bs4 import BeautifulSoup as bs

base_menu_url = "http://menuportal.dining.rutgers.edu/FoodPro/pickmenu.asp?locationNum={}&locationName={}&mealName={}&Name=Rutgers+University+Dining"


def get_menu_url(campus, meal="Lunch"):
  if campus == "New Brunswick":
    return base_menu_url.format("01", "Brower Commons", meal)
  elif campus == "Busch":
    return base_menu_url.format("04", "Busch Dining Hall", meal)
  elif campus == "Livingston":
    return base_menu_url.format("03", "Livingston Dining Commons", meal)
  elif campus == "CookDoug":
    return base_menu_url.format("05", "Neilson Dining Hall", meal)
  else:
    return None


class Menu():
  def __init__(self, campus, meal="Lunch"):
    self.campus = campus
    self.meal = meal
    self.data = self.__load_from_url__()

  def __load_from_url__(self):
    menu_url = get_menu_url(self.campus, self.meal)
    if not menu_url:
      return
    
    menu_items = []
    with requests.get(menu_url) as request:
      soup = bs(request.content)
      items = soup.find_all("div",{"class":"col-1"})
      for item in items:
        menu_items.append(item.text)

    return menu_items

  def serialize(self):
    return json.dumps(self.data)

if __name__ == "__main__":
  menu = Menu("Busch")
  print(menu.serialize())
