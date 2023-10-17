from fastapi import HTTPException, Header

def  verify_ghl_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token de autorizacion")

    # Verificar que el encabezado "Authorization" comience con "Bearer "
    token = authorization.replace("Bearer ", "")
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    # No es necesario retornar algo. El middleware pasara toda la informacion al "path-operator"
