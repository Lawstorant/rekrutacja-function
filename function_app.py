import azure.functions as func
import logging
import obtain_secret

app = func.FunctionApp()

@app.function_name(name="getsecret")
@app.route(route="getsecret", auth_level=func.AuthLevel.ANONYMOUS)
def getsecret(req: func.HttpRequest) -> func.HttpResponse:
    secret = obtain_secret.get_secret_value()
    code = 200

    # detect errors
    if secret[0] != None:
        code = 401

    response = func.HttpResponse(str(secret[1]), status_code=code)
    logging.info(f"Processed request. Status: {code}")
    
    return response
