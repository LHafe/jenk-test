from flask import Flask, request

## @package app
#  Aplicación Flask vulnerable usada para pruebas con Doxygen, Jenkins y CI/CD.

## Instancia principal de la aplicación Flask.
app = Flask(__name__)

@app.route('/')
def index():
    """!
    @brief Ruta principal del servidor.
    @return Mensaje de bienvenida de la aplicación.
    """
    return "Welcome to the vulnerable app!"


@app.route('/hello', methods=['GET'])
def hello():
    """!
    @brief Ruta que devuelve un saludo personalizado.
    
    Obtiene el parámetro 'name' desde la URL y devuelve un saludo dinámico.
    Ejemplo:
    @code
        /hello?name=Juan
    @endcode

    @return Mensaje de saludo con el nombre proporcionado.
    """
    name = request.args.get('name')
    return f'Hello, {name}!'

if __name__ == '__main__':
    """!
    @brief Punto de entrada de la aplicación Flask.
    
    Ejecuta el servidor en modo debug y escucha en todas las interfaces
    de red, puerto 5000.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
