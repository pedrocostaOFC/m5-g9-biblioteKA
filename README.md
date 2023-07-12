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