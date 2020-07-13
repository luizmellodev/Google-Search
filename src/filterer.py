import re

def applyGenericFilter(md):
	lines = re.sub('\!\[.*?\]\(.*?\)', '', md, flags=re.DOTALL).split('\n')

	lines = lines[lines.index('TIMESTAMPS')+1:]
	lines = [l.strip() for l in lines if len(l.strip())]

	tmp = [l.lower() for l in lines]
	lines = [l for l in lines if tmp.count(l.lower()) == 1]

	lines = [l for l in lines if '####' not in l]
	lines = [l for l in lines if l.count('*') % 2 == 0]

	lines = [l for l in lines if any([x.isalnum() for x in l])]
	return '\n'.join(lines)


def applyFolhaFilter(md):
	lines = md.split('\n')

	blanks = "ic_save,ic_share,Leia Mais,Voltar  Ver novamente".split(',')

	try:
		lines = lines[lines.index('Escuro')+1:]
		lines = lines[:lines.index('### sua assinatura pode valer ainda mais')]
	except:
		pass

	for blank in blanks:
		if blank in lines:
			lines.remove(blank)
	
	return '\n'.join(lines)


def applyEstadaoFilter(md):
	lines = md.split('\n')

	for i in range(len(lines)):
		if '#' in lines[0]:
			break
		del lines[0]

	lines = lines[:lines.index('Institucional')]

	if '### Comentários' in lines:
		lines = lines[:lines.index('### Comentários')]

	blanks = "Continuar lendo,Encontrou algum erro? Entre em contato,## Destaques em _Geral_".split(',')

	for blank in blanks:
		if blank in lines:
			lines.remove(blank)

	return '\n'.join(lines)