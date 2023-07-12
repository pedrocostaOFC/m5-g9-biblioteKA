<h1 align="center"> BiblioteKa - API </h1>


<h2>MVP - Produto Mínimo Viável</h2>


<h3>Empréstimo de Livros</h3>

<li>Cada livro tem um período fixo de empréstimo.</li>

<h3>Devolução de Livros</h3>

<li>Livros emprestados devem ter data de retorno.</li>

<li>Se a devolução cair em um fim de semana (sábado ou domingo), a data deve ser modificada para o próximo dia útil.</li>

<li>Estudantes que não devolverem o livro no prazo serão bloqueados de solicitar outros empréstimos.</li>

<h3>Bloqueio de Novos Empréstimos</h3>

<li>Estudantes com devoluções pendentes não podem emprestar mais livros até completar as devoluções.</li>

<li>O bloqueio deve permanecer por alguns dias após completar as devoluções.</li>

<h3>Usuários</h3>

<li>O sistema permite o cadastro de usuários, incluindo estudantes e colaboradores da biblioteca.</li>

<li>Usuários não autenticados podem acessar a plataforma para visualizar informações sobre os livros, como disponibilidade e título.</li>

<h3>Funcionalidades para estudantes:</h3>

<li>Visualizar histórico de livros emprestados.</li>

<li>Obter informações sobre livros.</li>

<li>Seguir um livro para receber notificações por email sobre disponibilidade e status.</li>

<h3>Funcionalidades para colaboradores:</h3>

<li>Cadastrar novos livros.</li>

<li>Emprestar livros.</li>

<li>Verificar histórico de empréstimos de estudantes.</li>

<li>Verificar status do estudante para determinar se está bloqueado de fazer um novo empréstimo por um período de tempo específico.</li>

# Sistema de Gerenciamento de Biblioteca

Este é um sistema de gerenciamento de biblioteca que permite o controle de empréstimos de livros, cadastro de usuários e colaboradores, e administração de cópias de livros.

## Funcionalidades Principais

- Cadastro de Usuários:
  - Apenas colaboradores da biblioteca podem criar novos usuários.
  - Os usuários podem ser estudantes ou colaboradores da biblioteca.
  - Usuários não autenticados podem acessar informações básicas sobre os livros, como disponibilidade e título.

- Empréstimo de Livros:
  - Cada livro pode ser emprestado por um período fixo de tempo.
  - Caso a devolução caia em um fim de semana (sábado ou domingo), a data de retorno é modificada para o próximo dia útil.
  - Estudantes que não devolvem os livros no prazo estipulado são impedidos de solicitar novos empréstimos.
  - Bloqueio de novos empréstimos: estudantes com devoluções pendentes não podem pegar mais livros emprestados até completar as devoluções.

- Controle de Livros:
  - Os colaboradores podem cadastrar novos livros no sistema.
  - É possível obter informações sobre os livros, como título e disponibilidade.
  - Histórico de empréstimos de cada estudante pode ser verificado pelos colaboradores.

## Endpoints

### Usuário

- **POST /user**: Cria um novo usuário. Somente colaboradores podem realizar essa ação.
- **GET /user**: Lista todos os usuários cadastrados.
- **GET /user/{id}**: Obtém informações sobre um usuário específico.
- **PATCH /user/{id}**: Atualiza informações de um usuário específico.
- **DELETE /user/{id}**: Deleta um usuário específico.

### Autenticação

- **POST /login**: Realiza o login de um usuário comum ou um super usuário.

### Livro

- **POST /book**: Cadastra um novo livro.
- **GET /book**: Lista todos os livros cadastrados.
- **GET /book/{id}**: Obtém informações sobre um livro específico.
- **DELETE /book/{id}**: Deleta um livro específico.

### Cópias

- **POST /copies**: Cria uma cópia de um livro, informando o ID do livro no corpo da requisição.
- **GET /copies/{id}**: Obtém informações sobre uma cópia específica.
- **DELETE /copies/{id}**: Deleta uma cópia específica.

### Empréstimo

- **POST /loan**: Realiza um novo empréstimo. Apenas colaboradores podem fazer isso. Deve-se fornecer o ID da cópia e do usuário. Usuários bloqueados não podem realizar empréstimos.
- **GET /loan**: Lista todos os empréstimos realizados.
- **PATCH /loan/{id}**: Marca um empréstimo como devolvido. Somente colaboradores podem fazer isso. Deve-se fornecer o campo "foi_devolvido" como true.

## Contribuição

Leonardo Cunha.
Artur Augusto.
Pedro Costa.
Renan Feliz.
