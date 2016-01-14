import argparse
import pickle


#g = open()
f = open('/home/txuma/Dropbox/LANCIS/Entrevistas/T-I052515_OTR.txt', 'r')
raw = f.read()

tokenized_text = raw.split(' ')


def remove_punctuation(tokens):
    text = []
    for token in tokens:
        token = token.replace(".","")
        token = token.replace(",","")
        token = token.replace("'", "")
        token = token.replace(";", "")
        token = token.replace("\n", "")
        token = token.replace("á", "a") 
        token = token.replace("é", "e")
        token = token.replace("í", "i")
        token = token.replace("ó", "o")
        token = token.replace("ú", "u")
        token = token.replace("ü", "u")
        token = token.replace("ñ", "n")
        token = token.replace("¿", "")
        token = token.replace("?", "")
        token = token.replace("(", "")
        token = token.replace(")", "")
        token = token.replace("\"", "")
        token = token.replace("…", "")
        token = token.replace("...", "")
        token = token.lower()
        text.append(token)
    return text


stopwords_es = ['a','ademas', 'ademas', 'ahi', 'ahi', 'al', 'alli', 'alli', 'alrededor', 'antano', 'ante', 'antes', 'apenas', 'aproximadamente', 'aquel', 'aquel', 'aquella', 'aquella', 'aquellas', 'aquellas', 'aquello', 'aquellos', 'aquellos', 'aqui', 'aqui', 'arriba', 'abajo', 'asi', 'asi', 'aun', 'aun', 'aunque', 'casi', 'como', 'con', 'conmigo', 'contigo', 'cual', 'cuales', 'cuales', 'cuando', 'cuando', 'cuanta', 'cuanta', 'cuantas', 'cuantas', 'cuanto', 'cuanto', 'cuantos', 'cuantos', 'de', 'debajo', 'del', 'delante', 'dentro', 'desde', 'despues', 'despues', 'detras', 'donde', 'donde', 'dos', 'durante', 'e', 'el', 'el', 'ella', 'ellas', 'ellos', 'en', 'enseguida', 'entre', 'es', 'esa', 'esa', 'esas', 'esas', 'ese', 'ese', 'eso', 'esos', 'esos', 'esta', 'esta', 'esta', 'estan', 'estan', 'estar', 'estas', 'estas', 'este', 'este', 'esto', 'estos', 'estos', 'ex', 'f', 'fue', 'fuera', 'fueron', 'g', 'h', 'ha', 'habia', 'habia', 'habla', 'hablan', 'hace', 'hacia', 'han', 'hasta', 'hay', 'incluso', 'junto', 'la', 'las', 'le', 'lo', 'los', 'luego', 'me', 'medio', 'mi', 'mi', 'mia', 'mia', 'mias', 'mias', 'mientras', 'mio', 'mio', 'mios', 'mios', 'mis', 'mismo', 'muy', 'n', 'no', 'nos', 'o', 'os', 'otra', 'otros', 'p', 'para', 'parte', 'pero', 'poco', 'por', 'porque', 'pronto', 'puede', 'q', 'qeu', 'que', 'que', 'quien', 'quien', 'quienes', 'quienes', 'quiza', 'quiza', 'quizas', 'quizas', 'r','repente', 's', 'salvo', 'se', 'se', 'segun', 'segun', 'sera', 'sera', 'si', 'si', 'sido', 'sin', 'sobre', 'solamente', 'solo', 'solo', 'son', 'soyos', 'su', 'supuesto', 'sus', 'suya', 'suyas', 'suyo', 't', 'tal', 'tambien', 'tambien', 'tampoco', 'te', 'ti', 'tiene', 'todavia', 'todavia', 'todo', 'todos', 'tras', 'tu', 'tu', 'tus', 'tuya', 'tuyas', 'tuyo', 'tuyos', 'u', 'un', 'una', 'unas', 'uno', 'unos', 'v', 'veces', 'vez', 'vosotras', 'vosotros', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'w', 'x', 'y', 'ya', 'z']


words = remove_punctuation(tokenized_text)

def stop_words(palabras):
    list_of_words = []
    for i in palabras:
        if i not in stopwords_es:
            list_of_words.append(i)
    return list_of_words


pickle.dump( stop_words( remove_punctuation(tokenized_text) ), open( 'test.p', 'wb'))
