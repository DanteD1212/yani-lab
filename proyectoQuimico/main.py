from flask import Flask, render_template, request
from conversiones import ( ##Importa el archivo conversiones el cual tiene todas las funciones que realizan conversiones
    gramos_a_kilogramos, kilogramos_a_gramos,
    celsius_a_fahrenheit, fahrenheit_a_celsius,
    litros_a_mililitros, mililitros_a_litros
)
from neubauer import Neubauer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/conversiones', methods=['GET', 'POST'])
def conversiones():
    resultado = None
    error = None
    valor = None
    unidad_origen = None
    unidad_destino = None
    tipo_unidad = None

    if request.method == 'POST':
        try:
            valor_str = request.form['valor']
            valor = float(valor_str)
            unidad_origen = request.form['unidad_origen']
            unidad_destino = request.form['unidad_destino']
            tipo_unidad = request.form['tipo_unidad']

            if tipo_unidad == 'masa':
                if unidad_origen == 'gramos' and unidad_destino == 'kilogramos':
                    resultado = gramos_a_kilogramos(valor)
                elif unidad_origen == 'kilogramos' and unidad_destino == 'gramos':
                    resultado = kilogramos_a_gramos(valor)
                elif unidad_origen == unidad_destino:
                    resultado = valor
                else:
                    error = "Conversión de masa no implementada."
            elif tipo_unidad == 'temperatura':
                if unidad_origen == 'celsius' and unidad_destino == 'fahrenheit':
                    resultado = celsius_a_fahrenheit(valor)
                elif unidad_origen == 'fahrenheit' and unidad_destino == 'celsius':
                    resultado = fahrenheit_a_celsius(valor)
                elif unidad_origen == unidad_destino:
                    resultado = valor
                else:
                    error = "Conversión de temperatura no implementada."
            elif tipo_unidad == 'volumen':
                if unidad_origen == 'litros' and unidad_destino == 'mililitros':
                    resultado = litros_a_mililitros(valor)
                elif unidad_origen == 'mililitros' and unidad_destino == 'litros':
                    resultado = mililitros_a_litros(valor)
                elif unidad_origen == unidad_destino:
                    resultado = valor
                else:
                    error = "Conversión de volumen no implementada."
            elif not tipo_unidad:
                error = "Por favor, selecciona un tipo de unidad."
            else:
                error = "Tipo de unidad no reconocido."

        except ValueError:
            error = "Por favor, ingresa un valor numérico válido."
        except KeyError:
            error = "Hubo un problema con los datos del formulario. Por favor, inténtalo de nuevo."

        return render_template('conversiones.html', resultado=resultado, error=error, valor=valor_str if 'valor' in locals() else '',
                               unidad_origen=unidad_origen, unidad_destino=unidad_destino,
                               tipo_unidad=tipo_unidad)
    return render_template('conversiones.html')


@app.route('/neubauer', methods=['GET', 'POST'])
def neubauer():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            num_cuadrantes = int(request.form['numCuadrantes'])
            volumen_cuadrante = float(request.form['volumenCuadrante'])
            factor_dilucion = float(request.form['factorDilucion'])
            celdas = []
            for i in range(1, num_cuadrantes + 1):
                celdas.append(int(request.form[f'celdasCuadrante{i}']))

            resultado = Neubauer.calcular_neubauer(num_cuadrantes, volumen_cuadrante, factor_dilucion, celdas)

        except ValueError:
            error = "Por favor, ingresa valores numéricos válidos."
        except KeyError:
            error = "Hubo un problema con los datos del formulario. Por favor, inténtalo de nuevo."

    return render_template('neubauer.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run() #debug=True cuando este editadno