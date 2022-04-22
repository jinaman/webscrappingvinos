import unittest
import main_carrefour
import main_changomas
import main_coto

loader = unittest.TestLoader()                #Necesito un loader, que es el lugar que va a cargar todas estas pruebas en nuestra suite.
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(main_carrefour))
suite.addTests(loader.loadTestsFromModule(main_coto))
suite.addTests(loader.loadTestsFromModule(main_changomas))

runner = unittest.TextTestRunner()#(verbosity=2)            # El runner es quien me va a ejecutar las cosas.  Le puedo poner el verbosity  = y un numeor para que me de más detalle, sino lo dejo vacío.

result = runner.run(suite)            # Lo ejecutamos y le mandamos las cosas a result
