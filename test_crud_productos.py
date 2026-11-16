import unittest

import crud_productos


class TestCrudProductos(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba: deja todo limpio."""
        crud_productos.productos.clear()
        crud_productos.siguiente_id = 1

    # ---------- CREAR ----------

    def test_crear_producto_exitoso(self):
        producto = crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)

        self.assertEqual(producto["id"], 1)
        self.assertEqual(producto["nombre"], "Cuaderno")
        self.assertEqual(len(crud_productos.productos), 1)

    def test_crear_producto_con_nombre_vacio(self):
        with self.assertRaises(ValueError):
            crud_productos.crear_producto("", "Cuaderno de 100 hojas", 5000, 20)

    def test_crear_producto_con_precio_negativo(self):
        with self.assertRaises(ValueError):
            crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", -1, 20)

    def test_crear_productos_tienen_id_unico(self):
        primero = crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)
        segundo = crud_productos.crear_producto("Lapicero", "Lapicero negro", 1500, 50)

        self.assertNotEqual(primero["id"], segundo["id"])

    # ---------- CONSULTAR ----------

    def test_consultar_producto_exitoso(self):
        crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)

        producto = crud_productos.consultar_producto(1)

        self.assertEqual(producto["nombre"], "Cuaderno")

    def test_consultar_producto_que_no_existe(self):
        with self.assertRaises(ValueError):
            crud_productos.consultar_producto(99)

    def test_listar_productos(self):
        crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)
        crud_productos.crear_producto("Lapicero", "Lapicero negro", 1500, 50)

        self.assertEqual(len(crud_productos.listar_productos()), 2)

    # ---------- ACTUALIZAR ----------

    def test_actualizar_producto_exitoso(self):
        crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)

        producto = crud_productos.actualizar_producto(1, "Cuaderno grande", "Cuaderno de 200 hojas", 8000, 15)

        self.assertEqual(producto["nombre"], "Cuaderno grande")
        self.assertEqual(producto["precio"], 8000)
        self.assertEqual(producto["cantidad"], 15)

    def test_actualizar_producto_que_no_existe(self):
        with self.assertRaises(ValueError):
            crud_productos.actualizar_producto(99, "Nombre", "Descripción", 1000, 5)

    def test_actualizar_producto_con_cantidad_negativa(self):
        crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)

        with self.assertRaises(ValueError):
            crud_productos.actualizar_producto(1, "Cuaderno", "Cuaderno de 100 hojas", 5000, -5)

    # ---------- ELIMINAR ----------

    def test_eliminar_producto_exitoso(self):
        crud_productos.crear_producto("Cuaderno", "Cuaderno de 100 hojas", 5000, 20)

        crud_productos.eliminar_producto(1)

        self.assertEqual(len(crud_productos.productos), 0)

    def test_eliminar_producto_que_no_existe(self):
        with self.assertRaises(ValueError):
            crud_productos.eliminar_producto(99)


if __name__ == "__main__":
    unittest.main()