 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/agilize/README.md
index 0000000000000000000000000000000000000000..b79d5e367b95ee60efb573cd3ced4ee8f395d3b6 100644
--- a//dev/null
+++ b/agilize/README.md
@@ -0,0 +1,12 @@
+# Agilize Backend
+
+Este diretório contém um exemplo simplificado do backend do sistema **Agilize**, um gerenciador de restaurantes com dashboard de caixa e controle de pedidos.
+
+## Como executar
+
+```bash
+pip install Flask
+python3 app.py
+```
+
+A aplicação ficará disponível em `http://localhost:5000`.
 
EOF
)
