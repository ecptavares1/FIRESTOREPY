import firebase_admin
from firebase_admin import credentials,firestore,db

cred = credentials.Certificate('ARQUIVO.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'URL FIRESTORE'
})

ref = db.reference('/')
ref.set({
    'USUARIOS' : {
        '101010' : {
            'Nome' : 'Python',
            'Idade' : '30',
            'Senha' : '123'
        }
    }
})