# Agilize Backend

Este diretório contém um exemplo simplificado do backend do sistema **Agilize**,
um gerenciador de restaurantes com dashboard de caixa e controle de pedidos.

O backend foi dividido em módulos independentes (Bluepr​​ints) para cada área
do restaurante:

- `modules/caixa` – rotas do caixa
- `modules/cozinha` – rotas da cozinha
- `modules/garcom` – rotas do garçom
- `modules/admin` – rotas administrativas

## Como executar

```bash
pip install Flask
python3 -m agilize
```

A aplicação ficará disponível em `http://localhost:5000`.

O acesso ao sistema exibe uma tela de login interativa com um fundo animado de
restaurante, demonstrado no arquivo `static/img/restaurant.gif`.

Após o login, o usuário é encaminhado para o painel principal. Funcionários
com funções específicas são redirecionados automaticamente para seu módulo
(garçom, caixa ou cozinha). O administrador visualiza um menu completo com
acesso a caixa, financeiro, relatórios, estoque e outras opções de gestão.
