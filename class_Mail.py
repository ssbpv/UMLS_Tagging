import datetime
import email.header

"""La classe Mail est dédiée au stockage des informations contenue
 dans chaque email.
  Elle contient les attributs suivants: sujet (subject),
  envoyeur (sender), date (date), et contenu (body)."""


class Mail(object):

    subject = ''  # Sujet de l'email
    sender = ''  # Envoyeur de l'email
    date = ''  # Date de l'email
    body = ''  # Contenu de l'email

    # Crée un objet Mail à partir d'un fichier f
    def __init__(self, f):
        with open(f, encoding="utf-8") as mail:
            bodyFound = False
            for line in mail:
                # Récupère toutes les lignes faisant partie du contenu
                # de l'email
                if bodyFound:
                    self.body += line
                # Récupère la ligne contenant le sujet et formate le resultat
                # (enlève les tags au début de la ligne, enlève le \n à la fin
                # de la ligne) et indique que le contenu commence
                if line.startswith('Subject: '):
                    tempSubject = line
                    # Enleve tous les tags de l'email a partir de la balise ']'
                    while tempSubject.find(']') != -1:
                        tempSubject = tempSubject[
                            tempSubject.find(']') + 1:]
                    tempSubject = tempSubject[1:len(tempSubject) - 1]
                    tempSubject = email.header.decode_header(tempSubject)
                    for s, e in tempSubject:
                        self.subject += s.decode('utf - 8')
                    bodyFound = True

                # Récupère la ligne contenant l'envoyeur et formate le resultat
                # (récupère seulement l'adresse mail contenue entre les '<>')
                if line.startswith('From: '):
                    self.sender = line[line.find('<') + 1:len(line) - 2]
                # Récupère la ligne contenant la date et formate le résultat en
                # un objet datetime
                if line.startswith('Date: '):
                    s = line[6:len(line) - 1].replace(" ", "")
                    s = s.replace(",", "")
                    s = s.replace(":", "")
                    self.date = datetime.datetime.strptime(
                        s, "%a%d%b%Y%H%M%S%z")

# Exemples d'utilisations de la classe
testMail = Mail('Documents/bioinfo_2014-01/2.recoded')
print('Subject: ', testMail.subject)
print('From: ', testMail.sender)
print('Date: ', testMail.date)
print('Body:', testMail.body)
