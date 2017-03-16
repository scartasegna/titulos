# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def impresos():
    db.t_resumen_impresos.id.readable = False
    #calculamos la cantidad total de impresos
    query = (db.t_resumen_impresos.f_impresos != 0)
    sum = db.t_resumen_impresos.f_impresos.sum()
    totalImpresos = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_resumen_impresos,deletable=False,editable=False)
    return dict(form=form,total=totalImpresos)

@auth.requires_login()
def auditados():
    db.t_resumen_auditados.id.readable = False
    #calculamos la cantidad total de egresados
    query = (db.t_resumen_auditados.f_auditados != 0)
    sum = db.t_resumen_auditados.f_auditados.sum()
    totalAuditados = db(query).select(sum).first()[sum]
    
    query = (db.t_resumen_auditados.f_aceptados != 0)
    sum = db.t_resumen_auditados.f_aceptados.sum()
    totalAceptados = db(query).select(sum).first()[sum]
    
    query = (db.t_resumen_auditados.f_rechazados != 0)
    sum = db.t_resumen_auditados.f_rechazados.sum()
    totalRechazados = db(query).select(sum).first()[sum]
    
    form = SQLFORM.grid(db.t_resumen_auditados,deletable=False,editable=False)
    return dict(form=form,total=totalAuditados,aceptados=totalAceptados,rechazados=totalRechazados)

@auth.requires_login()
def egresados():
    db.t_egresados.id.readable = False
    #calculamos la cantidad total de egresados
    query = (db.t_egresados.f_egresados != 0)
    sum = db.t_egresados.f_egresados.sum()
    totalEgresados = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_egresados,deletable=False,editable=False)
    return dict(form=form,total=totalEgresados)
