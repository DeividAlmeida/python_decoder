from django.http import JsonResponse, HttpResponse
import json
import magic

def validate_file_extension(file):
  valid_extension = "text/plain"
  file_extension = magic.from_buffer(file.read(1024), mime=True).lower()

  return file_extension.endswith(valid_extension)

def upload_file(request):
  if request.method == "POST":
    file = request.FILES.get("file")
    if file:
      if not validate_file_extension(file):
        return HttpResponse("Extensão de arquivo inválida.")
      else:
        data = {
          "message": "Arquivo recebido com sucesso.",
          "filename": file.name,
          "status": "success"
        }
        json_data = json.dumps(data)
        response = HttpResponse(json_data, content_type="application/json")
        
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