# devpy
from productos import productos
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def holaUsuario():
    return jsonify({
        "Mensaje": "Hola Mundo"
        })


# obtener todos los productos
@app.route("/productos")
def getProductos():
    return jsonify({
        "productos": productos, 
        "Mensaje": "Lista de Productos"
        })



# obtener un solo productos
@app.route("/productos/<string:nombre_producto>")
def getProducto(nombre_producto):
    productoEncontrado = [producto for producto in productos if producto["nombre"] == nombre_producto]
    # valida si un producto existe o no
    if len(productoEncontrado) > 0:
        return jsonify({"producto": productoEncontrado[0]})
    else:
        return jsonify({
            "Mensaje":"Producto no Encontrado"
            })


# agregar productos
@app.route("/productos", methods=["POST"])
def agregarProductos():
    producto_nuevo = {
        "nombre": request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"]
    }
    productos.append(producto_nuevo)
    return jsonify({
        "Mensaje": "Producto Agregado Exitosamente", 
        "Productos": productos
        })


# actualizar datos
@app.route("/productos/<string:nombre_producto>", methods=["PUT"])
def actualizarProductos(nombre_producto):
    productoEncontrado = [producto for producto in productos if producto["nombre"] == nombre_producto]
    if len(nombre_producto) > 0:
        productoEncontrado[0]["nombre"] = request.json["nombre"]
        productoEncontrado[0]["precio"] = request.json["precio"]
        productoEncontrado[0]["cantidad"] = request.json["cantidad"]
        return jsonify({
            "Mensaje": "Producto Actualizado",
            "Producto": productoEncontrado[0]
        })
    else:
        return jsonify({
            "Mensaje":"Error..."
        })


# eliminar producto
@app.route("/productos/<string:nombre_producto>", methods=["DELETE"])
def eliminarProducto(nombre_producto):
    productoEncontrado = [producto for producto in productos if producto["nombre"] == nombre_producto]
    if len(productoEncontrado) > 0:
        productos.remove(productoEncontrado[0])
        return jsonify({
            "Mensaje": "Producto Eliminado Exitosamente",
            "Productos": productos
        })
    else:
        return jsonify({
            "Mensaje": "Error No existe el Producto"
        })

# activamos el servidor
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)