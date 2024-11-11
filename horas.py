def seven_segmentify(time_: str):
  num = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    ':': ["   ", " . ", " . "],
    }
    
  hora, minuto = time_.split(":")
  primeiro_hora = ["   ", "   ", "   "] if hora[0] == '0' else num[hora[0]]
  segundo_hora = num[hora[1]]
  dois_pontos = num[':']
  primeiro_minuto = num[minuto[0]]
  segundo_minuto = num[minuto[1]]
    
  linha1 = primeiro_hora[0] + "" + segundo_hora[0] + "" + dois_pontos[0] + "" + primeiro_minuto[0] + "" + segundo_minuto[0]
  linha2 = primeiro_hora[1] + "" + segundo_hora[1] + "" + dois_pontos[1] + "" + primeiro_minuto[1] + "" + segundo_minuto[1]
  linha3 = primeiro_hora[2] + "" + segundo_hora[2] + "" + dois_pontos[2] + "" + primeiro_minuto[2] + "" + segundo_minuto[2]
  
  return f"{linha1}\n{linha2}\n{linha3}"
