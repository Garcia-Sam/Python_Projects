import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

email.To = 'macedo.samuel.garcia@gmail.com ; claragomesdf@gmail.com'

email.Subject = 'Teste de bot_email'

email.HTMLBody = '''<p>Me chamo Samuel Garcia, tenho 21 anos, moro em Brasília e tenho interesse em me</p>
<p>candidatar à vaga de estágio em TI.</p>

<p>Sou estudante de Tecnologia da Informação, tenho experiência em montagem e desmontagem de computadores,</p>
<p>noções de informática e programação na linguagem Python 3.</p>

<p>Tenho bastante facilidade de aprendizagem e muito a contribuir na empresa!</p>
<p>Segue em anexo meu currículo, e fico no aguardo de uma resposta.</p>

<p>Desde já agradeço.</p>

<p>At.te</p>
<p>Samuel Garcia </p> '''

email.send()
print('Email enviado!')
