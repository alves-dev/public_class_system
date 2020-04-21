# Class_system

### Orientações e Alterações:

- No arquivo settings.py, o banco de dados esta como o sqlite3. A um exemplo caso queira usar o postegresql na cloud da IMB ou da Google.

- Instalar os requerimentos seguindo as orientações do arquivo requiriments.txt

- Antes de rodar a aplicação temos que criar as tabelas no banco que estiver escolhido com:
    - python manage.py makemigrations
    - python manage.py migrate --run-syncdb
    
- Recomendo ler a documentação para sanar as duvidas [DJango](https://docs.djangoproject.com/pt-br/3.0/)    

##### Descrição de como se da o funcionamento do sistema:
   Foi baseado em uma regra de negócio onde a empresa 'test company' tem um sistema ERP e tem a necessidade de ter
        um material online para os funcionários de seus clientes.
        
   Regras:
   - Para acessar a plataforma de aulas o usuário deve se cadastrar informando o seu CPF e o CNPJ da empresa a qual
        trabalha.

   - O administrador deve confirmar que o usuário é funcionário da empresa em questão e realizar a liberação do seu
        usuário.

   - Após a liberação o usuário terá acesso as aulas onde ele pode escolher o tema e o sub-tema das aulas que
        deseja.

##### Description of how the system works:
   It was based on a business rule where the test company has an ERP system and needs to have
        online material for your customers' employees.

   Rules:
   
   - To access the class platform the user must register by informing his CPF and CNPJ of the company to which
        works.

   - The administrator must confirm that the user is an employee of the company in question and release his
        user.

   - After the release, the user will have access to the classes where he can choose the theme and sub-theme of the
        classes that want.