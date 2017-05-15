# -*- coding: utf-8 -*-
@auth.requires_membership('estadisticas')
def otro():
    """
    Gets all the data to display the number of Egresados by year in a cake graph
    """
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
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

@auth.requires_membership('estadisticas')
def auditadosPU():
    """
    Gets all the data to display the number of Egresados by year in a cake graph
    """
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
    query = (db.t_titulos_auditados.f_aceptados != 0)
    sum =db.t_titulos_auditados.f_aceptados.sum() + db.t_titulos_auditados.f_rechazados.sum()
    rows = db(query).select(*[sum,db.t_titulos_auditados.f_cargo],groupby=db.t_titulos_auditados.f_cargo)
    data = []
    labels = []
    print (rows)
    for r in rows:
        print(r)
        query = (db.auth_user.id == r.t_titulos_auditados.f_cargo)
        apellido =db.auth_user.last_name
        ape = db(query).select(apellido).first()[apellido]
        print(ape)
        data.append(r._extra[db.t_titulos_auditados.f_aceptados.sum() + db.t_titulos_auditados.f_rechazados.sum()])
        labels.append(ape)
    return dict(data=data,labels=labels)

@auth.requires_membership('estadisticas')
def auditados():
    """
    Gets all the data to display the number of Auditados (aceptados and rechazados) per day in a cake graph
    """
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
    #calculamos la cantidad total de impresos
    query = (db.t_resumen_auditados.f_auditados != 0)
    sum = db.t_resumen_auditados.f_auditados.sum()
    totalAuditados = db(query).select(sum).first()[sum]
    todos = db.t_resumen_auditados
    rows = db(todos).select()
    dataAceptado = []
    colorAceptadoBack = []
    colorAceptadoLine = []
    dataRechazado = []
    colorRechazadoBack = []
    colorRechazadoLine = []
    labels = []
    print (rows)
    for r in rows:
        dataAceptado.append(r.f_aceptados)
        dataRechazado.append(r.f_rechazados)
        colorAceptadoBack.append('rgba(9, 151, 193, 0.2)')
        colorAceptadoLine.append('rgba(9, 151, 193,1)')
        labels.append(r.f_fecha)
    return dict(dataA=dataAceptado,dataB=dataRechazado,colorA1=colorAceptadoBack,colorAL=colorAceptadoLine,labels=labels,total=totalAuditados)
