from .calculator import calculate
from .search import search
from .remind import remind


routes = {
    "calculate": calculate,
    "search": search,
    "remind": remind
}

def handle(intent, para):
    method = routes[intent]
    return method(*para)