class Router(object):
    url_dict = {}

    def bind(self, url, method, action):
        self.url_dict[(url, method)] = action

    def runRequest(self, url, method):
        if (url, method) in self.url_dict:
            result = self.url_dict[(url, method)]()
        else:
            result = "Error 404: Not Found"
        return result




router = Router()

print(router.bind('/hello', 'GET', lambda: 'hello world'))
print(router.runRequest('/hello', 'GET'))