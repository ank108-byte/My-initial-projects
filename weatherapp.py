import sys
import requests
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QVBoxLayout,QApplication
from PyQt5.QtCore import Qt
class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app by Anuj!!!!")
        self.city_name=QLabel("Enter city name:",self)
        self.line_edit=QLineEdit(self)
        self.get_button=QPushButton("Get Weather",self)
        self.city_temperature=QLabel(self)
        self.emoji_label=QLabel(self)
        self.temperature_description=QLabel(self)
        self.initUI()
    def initUI(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_name)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.get_button)
        vbox.addWidget(self.city_temperature)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.temperature_description)
        self.setLayout(vbox)
        self.city_name.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)
        #self.get_button.setAlignment(Qt.AlignCenter)
        self.city_temperature.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.temperature_description.setAlignment(Qt.AlignCenter)
        self.city_name.setObjectName("city_name")
        self.line_edit.setObjectName("line_edit")
        self.get_button.setObjectName("get_button")
        self.city_temperature.setObjectName("city_temperature")
        self.emoji_label.setObjectName("emoji_label")
        self.temperature_description.setObjectName("temperature_description")
        self.setStyleSheet("""
                           QLabel,QPushButton{
                           font-family:calibri;
                           }
                           QLabel#city_name{
                           font-style:italic;
                           font-size:50px;}
                           QPushButton#get_button{
                           font-size:40px;
                           font-weight:bold;
                           }
                           QLabel#city_temperature{
                           font-size: 70px;}
                           QLabel#emoji_label{
                           font-size:100px;
                           font-family:segoe UI emoji;
                           }
                           QLineEdit#line_edit{
                           font-size:40px;} 
                           QLabel#temperature_description{
                           font-size:40px;}                 
                        """)
        self.get_button.clicked.connect(self.getweather)
    def getweather(self):
        api_key="774b8fd577703f0ed5dfadd7ddfd5e00"
        city=self.line_edit.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway timeout:\nNo response from server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self,message):
        self.city_temperature.setStyleSheet("font-size:30px;")
        self.city_temperature.setText(message)
        self.emoji_label.clear()
        self.temperature_description.clear()
    def display_weather(self,data):
        self.city_temperature.setStyleSheet("font-size:70px;")
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k-273.15
        weather_id=data["weather"][0]["id"]
        #print(data)
        weather_description=data["weather"][0]["description"]
        self.city_temperature.setText(f"{temperature_c:.2f}°C")
        self.emoji_label.setText(self.getweatheremoji(weather_id))
        self.temperature_description.setText(weather_description)
    @staticmethod
    def getweatheremoji(weather_id):
        if 200 <= weather_id <= 232:
            return"⛈️"
        elif 300 <= weather_id <= 321:
            return"🌦️"
        elif 500 <= weather_id <= 531:
            return"🌧️"
        elif 600 <= weather_id <= 622:
            return"❄️"
        elif 701 <= weather_id <= 741:
            return"🌫️"
        elif weather_id == 751:
            return"🏜️"
        elif weather_id == 761:
            return"🌪️"
        elif weather_id == 762:
            return"🌋"
        elif weather_id == 771:
            return"💨"
        elif weather_id == 781:
            return"🌪️"
        elif weather_id == 800:
            return"☀️"
        elif 801 <= weather_id <= 804:
            return"☁️"
        else:
            return""
if __name__=="__main__":
    app=QApplication(sys.argv)
    weatherapp=weather_app()
    weatherapp.show()
    sys.exit(app.exec_())