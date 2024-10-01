from fastapi import FastAPI, Request, Depends, Cookie, HTTPException, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bibiotheques import Bibliotheques
from livre import Livre
from journal import Journal
from dvd import Dvd
from personne import Personne

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wm7ze*2b",
    "database": "bu",
}

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dependency to get the user's login and name from cookies
def get_user_data(login: str = Cookie(None), nom: str = Cookie(None)):
    return login, nom

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, user_data: tuple = Depends(get_user_data)):
    datas = Bibliotheques(config).get_all_document()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "livres": datas["livre"],
        "journals": datas["journal"],
        "dvds": datas["dvd"],
        "login": user_data[0],
        "nom": user_data[1],
    })

@app.get("/livre/{cote}", response_class=HTMLResponse)
async def livre(cote: str, request: Request, user_data: tuple = Depends(get_user_data)):
    data = Livre.get(config, cote)
    return templates.TemplateResponse("livre.html", {
        "request": request,
        "cote": data[0][0],
        "salle": data[0][1],
        "titre": data[0][2],
        "auteur": data[0][3],
        "sur_place": data[0][4],
        "online": data[0][5],
        "debut_emprunt": data[0][6],
        "fin_emprunt": data[0][7],
        "login": user_data[0],
        "nom": user_data[1],
    })

@app.get("/dvd/{cote}", response_class=HTMLResponse)
async def dvd(cote: str, request: Request, user_data: tuple = Depends(get_user_data)):
    data = Dvd.get(config, cote)
    return templates.TemplateResponse("dvd.html", {
        "request": request,
        "cote": data[0][0],
        "salle": data[0][1],
        "titre": data[0][2],
        "auteur": data[0][3],
        "sur_place": data[0][4],
        "online": data[0][5],
        "debut_emprunt": data[0][6],
        "fin_emprunt": data[0][7],
        "login": user_data[0],
        "nom": user_data[1],
    })

@app.get("/journal/{cote}", response_class=HTMLResponse)
async def journal(cote: str, request: Request, user_data: tuple = Depends(get_user_data)):
    data = Journal.get(config, cote)
    return templates.TemplateResponse("journal.html", {
        "request": request,
        "cote": data[0][0],
        "salle": data[0][1],
        "titre": data[0][2],
        "date_publication": data[0][3],
        "sur_place": data[0][4],
        "online": data[0][5],
        "debut_emprunt": data[0][6],
        "fin_emprunt": data[0][7],
        "login": user_data[0],
        "nom": user_data[1],
    })

@app.get("/auth", response_class=HTMLResponse)
async def auth_get(request: Request, login: str = Cookie(None)):
    if login:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/auth", response_class=RedirectResponse)
async def auth_post(login: str = Form("login"), password: str = Form("password")):
    if Personne.connection(config, login, password):
        data = Personne.get(config, login)
        response = RedirectResponse(url="/", status_code=302) # status code important sinon le middle renvoie en post
        response.set_cookie(key="num", value=str(data[0][0]))
        response.set_cookie(key="login", value=login)
        return response
    else:
        return RedirectResponse(url="/auth")

@app.get("/user", response_class=HTMLResponse)
async def user(request: Request, login: str = Cookie(None)):
    if login:
        user_data = Personne.get(config, login)
        return templates.TemplateResponse("user.html", {
            "request": request,
            "num": user_data[0][0],
            "perm": user_data[0][1],
            "nom": user_data[0][2],
            "prenom": user_data[0][3],
            "login": user_data[0][4],
            "password": user_data[0][5],
        })
    else:
        return RedirectResponse(url="/auth")

@app.get("/logout", response_class=RedirectResponse)
async def logout():
    response = RedirectResponse(url="/auth")
    response.delete_cookie("num")
    response.delete_cookie("login")
    return response

# Run with: uvicorn your_file_name:app --host 0.0.0.0 --port 5000
