# -*- coding: utf-8 -*-
# intente algo como
def egresados():
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
    return dict( title='Charts!')

def otro():
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
    #calculamos la cantidad total de impresos
    query = (db.t_egresados.f_egresados != 0)
    sum =db.t_egresados.f_egresados.sum()
    totalEgresados = db(query).select(sum).first()[sum]
    todos = db.t_egresados.id > 0
    rows = db(todos).select()
    data = []
    labels = []
    print (rows)
    for r in rows:
        data.append(r.f_egresados)
        labels.append(r.f_anio)
    return dict(data=data,labels=labels,total=totalEgresados)
