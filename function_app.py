import azure.functions as func
import logging
import obtain_secret

app = func.FunctionApp()

@app.function_name(name="showsecret")
@app.route(route="showsecret", auth_level=func.AuthLevel.ANONYMOUS)
def showsecret(req: func.HttpRequest) -> func.HttpResponse:
    secret = obtain_secret.get_secret_value()
    code = 200
        
    res_body = "Application version: "
    with open('application.version', 'r') as file:
        res_body += file.readline()
    
    # detect errors
    if secret[0] != None:
        code = 401
    else:
        res_body += f"{str(secret[1])}"

    response = func.HttpResponse(res_body, status_code=code)
    logging.info(f"Processed request. Status: {code}")
    
    return response
