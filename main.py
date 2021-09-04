from kivy.app import App
from kivy.uix.codeinput import CodeInput
import os
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from pygments.lexers import HtmlLexer , CssLexer
class FastCodeApp(App):
	def build(self):
		#Проверка на существование файлов
		#Файл "index.html"
		file1 = os.path.exists("index.html")
		if(file1 == False):
			fileHtml = open("index.html" , "w")
			fileHtml.write("<!--FastCode 1.0 -- HTML--!>\n")
			fileHtml.close()
		#Файл "style.css"
		file2 = os.path.exists("style.css")
		if(file2 == False):
			fileCss = open("style.css" , "w")
			fileCss.write("\n")
			fileCss.close()
		#Создание главного виджета BoxLayout	
		bl = BoxLayout(padding = 3 , spacing = 3)
		#Функция для сохранения файлов
		def save(text1 , text2):
			#Файл "index.html"
			file = open("index.html" , "w")
			file.write(text1)
			file.close()
			#Файл "style.css"
			file2 = open("style.css" , "w")
			file2.write(text2)
			file2.close()
		#Получение данных из файлов
		htmlFile = open("index.html")
		textHtml = htmlFile.read()
		cssFile = open("style.css")
		textCss = cssFile.read()
		#Создание полей ввода кода
		self.html = CodeInput(lexer = HtmlLexer() , text = textHtml)
		self.css = CodeInput(lexer = CssLexer() , text = textCss )
		#Кнопка сохранения файлов
		save_button = Button(text = "Сохранить" , size_hint = [.3 , .5] , on_press = lambda x:save(self.html.text , self.css.text))
		#Добавление виджетов
		bl.add_widget(self.css)
		bl.add_widget(self.html)
		bl.add_widget(save_button)
		#Результат
		return bl
if __name__ == '__main__':
	FastCodeApp().run()