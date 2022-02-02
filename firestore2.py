from google.cloud import firestore

db = firestore.Client()
doc_ref = db.collection(u'users').document(u'Nome')
doc_ref.set({
    u'First' : u'Eduardo',
    u'Last' : u'Tavares',
    u'email'  : 'chambinho@djchambinho.com'
})

user_ref = db.collection(u'users')
for doc in user_ref.stream():
    print(u'{}=>{}'.format(doc.id,doc.to_dict()))