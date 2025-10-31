# Backgammon

**Nombre:** Joaquín Aubone

---

## 🚀 Cómo Ejecutar

### Requisitos:
- Python 3.8 o superior

### 1) Instalar las librerías y dependencias (hacer en entorno virtual)
```bash
pip install -r requirements.txt
```

### 2) Ejecutar el juego

```bash
python -m main
```

### 3) Correr los tests + coverage
```bash
python -m unittest discover tests/
coverage run -m unittest discover -s . -p "test*.py"
coverage report -m