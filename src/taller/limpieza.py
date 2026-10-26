import pandas as pd


def filtrar_duracion(
    df: pd.DataFrame,
    minimo: float = 1.0,
    maximo: float = 60.0,
) -> pd.DataFrame:
    """Deja solo los viajes con duracion en [minimo, maximo] minutos."""
    return df[
        (df["duration"] >= minimo)
        & (df["duration"] <= maximo)
    ].reset_index(drop=True)