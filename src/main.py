from commands import execute
from recognize import listen, transcript

rec_input = transcript(listen())
if not rec_input:
    print("[X] não foi retornado uma entrada")
execute(rec_input)
