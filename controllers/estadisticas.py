# -*- coding: utf-8 -*-

@auth.requires_membership('estadisticas')
def impresos():
    db.t_resumen_impresos.id.readable = False
    #calculamos la cantidad total de impresos
    query = (db.t_resumen_impresos.f_impresos != 0)
    sum = db.t_resumen_impresos.f_impresos.sum()
    totalImpresos = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_resumen_impresos,deletable=False,editable=False,orderby=~db.t_resumen_impresos.f_fecha)
    return dict(form=form,total=totalImpresos)

@auth.requires_membership('estadisticas')
def auditados():
    db.t_resumen_auditados.id.readable = False
    #calculamos la cantidad total de auditados
    query = (db.t_resumen_auditados.f_auditados != 0)
    sum = db.t_resumen_auditados.f_auditados.sum()
    totalAuditados = db(query).select(sum).first()[sum]
    #Total Aceptados
    query = (db.t_resumen_auditados.f_aceptados != 0)
    sum = db.t_resumen_auditados.f_aceptados.sum()
    totalAceptados = db(query).select(sum).first()[sum]
    #Total Rechazados
    query = (db.t_resumen_auditados.f_rechazados != 0)
    sum = db.t_resumen_auditados.f_rechazados.sum()
    totalRechazados = db(query).select(sum).first()[sum]
    form = SQLFORM.grid(db.t_resumen_auditados,deletable=False,editable=False,orderby=~db.t_resumen_auditados.f_fecha)
    return dict(form=form,total=totalAuditados,aceptados=totalAceptados,rechazados=totalRechazados)

@auth.requires_membership('estadisticas')
def egresados():
    db.t_egresados.id.readable = False
    #calculamos la cantidad total de egresados
    query = (db.t_egresados.f_egresados != 0)
    sum = db.t_egresados.f_egresados.sum()
    totalEgresados = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_egresados,deletable=False,editable=False,orderby=~db.t_egresados.f_anio)
    return dict(form=form,total=totalEgresados)