import pandas as pd

from taller.limpieza import filtrar_duracion


def test_filtra_fuera_de_rango():
    df = pd.DataFrame({"duration": [0.5, 10.0, 30.0, 90.0]})
    resultado = filtrar_duracion(df)
    assert list(resultado["duration"]) == [10.0, 30.0]


def test_no_modifica_el_original():
    df = pd.DataFrame({"duration": [0.5, 10.0]})
    filtrar_duracion(df)
    assert len(df) == 2
