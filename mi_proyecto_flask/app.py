from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta Principal (Menú)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta Ejercicio 1 (Cálculo de compras)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        
        # Lógica de negocio
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro
        
        # Calcular descuento según la edad
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0
            
        total_a_pagar = total_sin_descuento - descuento
        
        # Crear diccionario con resultados para enviar a la plantilla
        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_a_pagar': total_a_pagar
        }
        
    return render_template('ejercicio1.html', resultado=resultado)

# Ruta Ejercicio 2 (Inicio de sesión)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        # Lógica de validación
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = "Bienvenido Administrador juan"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
            
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)