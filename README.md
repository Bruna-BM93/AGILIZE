# AGILIZE
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
python3 -m agilize.app
```

A aplicação ficará disponível em `http://localhost:5000`.