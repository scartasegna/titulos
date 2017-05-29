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

@auth.requires_membership('estadisticas')
def impresosPR():
    """
    Gets all the data to display the number of Impresos by Region in a bar graph
    """
    response.files.append('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js')
    query = (db.t_resumen_impresos.id != 0)
    sum1= db.t_resumen_impresos.f_sum_region1.sum()
    sum2= db.t_resumen_impresos.f_sum_region2.sum()
    sum3= db.t_resumen_impresos.f_sum_region3.sum()
    sum4= db.t_resumen_impresos.f_sum_region4.sum()
    sum5= db.t_resumen_impresos.f_sum_region5.sum()
    sum6= db.t_resumen_impresos.f_sum_region6.sum()
    sum7= db.t_resumen_impresos.f_sum_region7.sum()
    sum8= db.t_resumen_impresos.f_sum_region8.sum()
    sum9= db.t_resumen_impresos.f_sum_region9.sum()
    sum10= db.t_resumen_impresos.f_sum_region10.sum()
    sum11= db.t_resumen_impresos.f_sum_region11.sum()
    sum12= db.t_resumen_impresos.f_sum_region12.sum()
    sum13= db.t_resumen_impresos.f_sum_region13.sum()
    sum14= db.t_resumen_impresos.f_sum_region14.sum()
    sum15= db.t_resumen_impresos.f_sum_region15.sum()
    sum16= db.t_resumen_impresos.f_sum_region16.sum()
    sum17= db.t_resumen_impresos.f_sum_region17.sum()
    sum18= db.t_resumen_impresos.f_sum_region18.sum()
    sum19= db.t_resumen_impresos.f_sum_region19.sum()
    sum20= db.t_resumen_impresos.f_sum_region20.sum()
    sum21= db.t_resumen_impresos.f_sum_region21.sum()
    sum22= db.t_resumen_impresos.f_sum_region22.sum()
    sum23= db.t_resumen_impresos.f_sum_region23.sum()
    sum24= db.t_resumen_impresos.f_sum_region24.sum()
    sum25= db.t_resumen_impresos.f_sum_region25.sum()
    rows = db(query).select(*[sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10, sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19, sum20, sum21, sum22, sum23, sum24, sum25])
    dataOrdenada=[0 for i in range(25)]
    labelsOrdenada=[0 for i in range(25)]
    for r in rows:
        i=1
        for campo in r._extra:
            region = traducirNombreFeoALindo(campo)
            indice= int(region)-1
            labelsOrdenada[indice]= "Region %s" %(region)
            dataOrdenada[indice]= r._extra[campo]
            i+=1
    return dict(data=dataOrdenada,labels=labelsOrdenada)

def traducirNombreFeoALindo(campoBase):
    reg= campoBase[-3:-1]
    if reg[0] == 'n':
        reg = reg[1]
    return reg
