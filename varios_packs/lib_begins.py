import begin


@begin.start
def main(param1, param2, param3="default"):
    """Begins te ayuda a crear scripts de línea de comandos,
    con argumentos posicionales y opcionales, con ayuda automática.
    """
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    print(f"param3: {param3}")
