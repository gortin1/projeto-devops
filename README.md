# 📦 Projeto DevOps - API Flask com CI/CD

Este projeto demonstra uma **integração CI/CD** de uma API em **Flask** (Python), com **containerização via Docker** e deploy automático via GitHub Actions e Render.

---

## 🔍 Visão Geral

- API desenvolvida em **Python/Flask**
- Containerizada usando **Docker**
- Orquestrada por **docker-compose**
- Pipeline **CI/CD** com GitHub Actions (build → test → deploy)
- Deploy automático configurado no **Render.com**

---

## 🧩 Estrutura do Projeto

```
/
├── .github/workflows/     # CI/CD com GitHub Actions
│   └── python-app.yml
├── app/                    # Código-fonte principal da API
│   ├── static/            # Arquivos estáticos
│   ├── tests/             # Testes automatizados
│   └── app.py             # Aplicação Flask
│   
├── Dockerfile             # Imagem Docker da API
├── docker-compose.yml     # Orquestração local com Docker Compose
├── requirements.txt   # Dependências Python
└── README.md              
```

---

## 🚀 Executando localmente

### Pré-requisitos
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Build da imagem
```bash
docker-compose build
```

### 2. Subir o serviço
```bash
docker-compose up
```

A API estará disponível em `http://localhost:1313`.  
Endpoints e documentação Swagger estão em `http://localhost:1313/static/swagger`.

---

## 🔄 Pipeline CI/CD

A pipeline executa:

1. **build** – cria a imagem Docker.
2. **test** – executa testes na imagem.
3. **deploy** – envia automaticamente para o Render se os testes passarem com sucesso.

💡 O status da pipeline aparece no GitHub Actions após cada push na branch `main`.

---
## 🧠 Tecnologias utilizadas

- **Python**
- **Flask**
- **SQLite** (quando aplicável)
- **Docker & Docker Compose**
- **GitHub Actions**
- **Render.com** para deploy automático

---

## 📌 Contato

Dúvidas ou sugestões? Abra uma issue ou entre em contato via GitHub.

---

> Proposto por **gortin1**, para estudo e demonstração de práticas de DevOps com CI/CD e automação.
