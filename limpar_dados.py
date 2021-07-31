from bs4 import BeautifulSoup
from ast import literal_eval
import sys
import json

def sanitizar_saida(arq):

  file = open(arq, 'r')
  html_file = file.read()
  file.close()

  soup = BeautifulSoup(html_file, 'html.parser')
  materias_html = soup.find_all('tr')

  materias = {}

  for i in materias_html:
    soup = BeautifulSoup(str(i), 'html.parser')
    materias_html_td = i.find_all('td')

    disciplina_soup = materias_html_td[1]
    disciplina = disciplina_soup.get_text().replace('\n', '').strip().replace('  ', '')
    materias[disciplina] = {}
    nota = 1
    materia_medias_ref = [materias_html_td[7], materias_html_td[9], materias_html_td[11], materias_html_td[13], materias_html_td[15], materias_html_td[18]]
    for value in materia_medias_ref:
      materias[disciplina]['nota_' + str(nota)] = []
      soup = BeautifulSoup(str(value), 'html.parser')
      materias[disciplina]['nota_' + str(nota)].append(soup.get_text().replace(' ', '').replace('\n', '').replace('\\n', ''))
      nota += 1
  return materias


dic_materias = sanitizar_saida("boletim_html.txt")
with open('boletim.json', 'w') as arq:
  arq.write(
    json.dumps(dic_materias, sort_keys=True, indent=2, ensure_ascii=False)
  )

