from stacks import StackDeque


class Browser:

    def __init__(self):
        self.__back_history = StackDeque()
        self.__front_history = StackDeque()
        self.__current_page = None

    def visit(self, page):
        if self.__current_page is not None:
            self.__back_history.push(self.__current_page)
        self.__current_page = page
        # Clean the front history to vist a new page.
        self.__front_history = StackDeque()

    def back(self):
        if self.__back_history.is_empty():
            print("Empty history")
            return
        self.__front_history.push(self.__current_page)
        self.__current_page = self.__back_history.pop()

    def front(self):
        if self.__front_history.is_empty():
            print("Empty history")
            return
        self.__back_history.push(self.__current_page)
        self.__current_page = self.__front_history.pop()

    @property
    def current_page(self):
        if self.__current_page is not None:
            return self.__current_page
        else:
            return "No pages visited"


# Example:
browser = Browser()

browser.visit("pagina1.com")
print(browser.current_page)  # Prints "pagina1.com".

browser.visit("pagina2.com")
print(browser.current_page)  # Prints "pagina2.com".

browser.back()
print(browser.current_page)  # Prints "pagina1.com".

browser.front()
print(browser.current_page)  # Prints "pagina2.com".

browser.back()
browser.back()  # Prints "Empty history".
