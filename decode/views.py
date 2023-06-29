from django.http import HttpResponse
import json
from .utils import validate_file_extension
from .controllers import *

def upload_file(request):
  if request.method == "POST":
    file = request.FILES.get("file")
    if file:
      if not validate_file_extension(file):
        return HttpResponse("Extensão de arquivo inválida.")
      else:
        
        digits = transform_file_to_array(file)
        frequency = count_digits_frequency(digits)
        password = rank_digits_by_score(frequency)

        response = HttpResponse(password, content_type="application/json")
        
        return response
    else:
      data = {
        "message": "Nenhum arquivo enviado.",
        "status": "error"
      }
      json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
      response = HttpResponse(json_data, status=405, content_type="application/json; charset=utf-8")
      return response

  else:
    data = {
      "message": "Método HTTP não permitido.",
      "status": "error"
    }
    json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    response = HttpResponse(json_data, status=405, content_type="application/json; charset=utf-8")
    return response