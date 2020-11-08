import json
import requests
from Driver.ServerManipulation import ServerManipulator


class WebDriver():
    def __init__(self,browser,port='8500'):
        self.port = port
        self.browser = browser
        self.capabilities = {}
        self.url = 'http://127.0.0.1:'+self.port+"/"
        self.session = ""
        self.server_manipulation = ServerManipulator()


    def start_browser(self, browser= 'chrome', capabilities = {}):

        self.server_manipulation.open_server(browser,self.port)
        self.session = self.create_session(capabilities)

    def navigate(self,url):
        try:
            myJson = {"url": url}
            navigation_url = self.url+"session/"+self.session+"/url"
            print("Pointing to: "+navigation_url)
            response = requests.request("POST", navigation_url, data=json.dumps(myJson).encode("utf8"))
        except:
            print("Something went on navigation")
            self.end_session(self.session)

    def close_browser(self):
        close_url = self.url+"session/"+self.session+"/window"
        requests.request("DELETE",close_url)

    '''
    def open_server(self,server):
        # Open the server in a subprocess. Which server will open depends on the browser you want to use
        if str.upper(server) == "CHROME":
            #self.process = subprocess.Popen("chromedriver.exe --verbose --port=9000")
            self.process = subprocess.Popen("chromedriver.exe --port=9000")
            return self.process
    '''
    def create_session(self,capabilities):
        if capabilities == {}:
            capabilities = {
                "desiredCapabilities": {
                    "browserName": "chrome",
                    "chromeOptions": {
                        "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    },
                   "platform": "ANY"
               }
            }
        try:

            session_url = self.url+"session"
            response = requests.request("POST", session_url, data=json.dumps(capabilities).encode('utf8'))
            return json.loads(response.text)['sessionId']
        except:
            self.end_session()

    def end_session(self):
        requests.request("DELETE",self.url+"/session"+self.session)
        requests.delete(self.url+"/session"+self.session)

    # Finishing the process that execute the chromeDiver and close the port 9000
    def end_driver(self):
        print("Finishing webdriver server...")
        self.process.terminate()


    # -----------------BROWSER SIZE---------------------
    def close_browser(self):
        close_url = self.url+"session/"+self.session+"/window"
        requests.request("DELETE",close_url)

    def max_browser(self):
        max_url = self.url+"session/"+self.session+"/window/maximize"
        my_json = {'value':'maximize'}
        #self.requester.post(max_url,my_json)
        response = requests.request("POST",max_url,data=json.dumps(my_json).encode('utf-8'))

    def min_browser(self):
        min_url = self.url + "session/" + self.session + "/window/minimize"
        my_json = {'value': 'minimize'}
        response = requests.request("POST", min_url, data=json.dumps(my_json).encode('utf-8'))

    def full_screen_browser(self):
        fs_url = self.url + "session/" + self.session + "/window/fullscreen"
        my_json = {'value': 'fullscreen'}
        response = requests.request("POST", fs_url, data=json.dumps(my_json).encode('utf-8'))

    def set_browser_size(self,height,width):
        browser_size_url = self.url+"session/"+self.session+"/window/rect"
        my_json = {'width': width,'height': height}
        response = requests.request("POST", browser_size_url, data=json.dumps(my_json).encode('utf-8'))

    # ----------------END OF BROWSER SIZES--------------------------------------------------
    def get_status(self):
        status_url = self.url + "status"
        response = requests.get(status_url)
        print("--STATUS---------")
        print(response.text)
        print("-----------------")
        return response.text

        # ELEMENT MANIPULATION

    def locate_element(self, location_type, location_value):
        """
        Locates an element.
        :param location_type: Type of location (id, name, etc)
        :param location_value: the locator itself.
        :return: the element.
        :author: Stiven
        """
        element_url = self.url + "session/" + self.session + "/element"
        my_json = {'using': location_type, 'value': location_value}
        response = requests.request("POST", element_url, data=json.dumps(my_json).encode('utf-8'))
        print(json.loads(response.text)['value'])
        return json.loads(response.text)['value']['ELEMENT']

    def write(self,element,text):
        """
        Writes something in a web element
        :param element: The element where the text will be writen
        :param text: The text that will go.
        :return:
        """
        write_url = self.url + "session/" + self.session +"/element/"+element+"/value"
        my_json = {'value': [text]}
        # Write the element that i give it
        response = requests.request("POST", write_url, data=json.dumps(my_json).encode('utf-8'))

    def click(self,element):
        """
        Clicks on an element
        :param element: The element to be clicked
        :return:
        """
        write_url = self.url + "session/" + self.session + "/element/" + element + "/click"
        my_json = {'value': 'click'}
        response = requests.request("POST", write_url, data=json.dumps(my_json).encode('utf-8'))


    def get_element_text(self,element):
        """
        Gets an element text
        :param element: The element to get the text
        :return:
        """
        text_url = self.url + "session/" + self.session + "/element/"+element+"/text"
        response = requests.request("GET",text_url)
        return json.loads(response.text)['value']
        #return json.loads(self.requester.get(self.url + "session/" + self.session + "/element/"+element+"/text").text)['value']

    # MAYBE METHODS BELOW SHOULD GO IN A SEPARATE CLASS?

    def create_session(self, capabilities):
        if capabilities == {}:
            capabilities = {
                "desiredCapabilities": {
                    "browserName": "chrome",
                    "chromeOptions": {
                        "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    },
                    "platform": "ANY"
                }
            }
        try:

            session_url = self.url + "session"
            response = requests.request("POST", session_url, data=json.dumps(capabilities).encode('utf8'))
            return json.loads(response.text)['sessionId']
        except:
            self.end_session()


    def end_session(self):
        requests.delete(self.url + "/session" + self.session)
