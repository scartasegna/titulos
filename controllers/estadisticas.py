# -*- coding: utf-8 -*-

@auth.requires_membership('estadisticas')
def impresos():
    """
    Gets all the data to display the number of Impresos per day from the resumen_impresos table
    """
    db.t_resumen_impresos.id.readable = False
    query = (db.t_resumen_impresos.f_impresos != 0)
    sum = db.t_resumen_impresos.f_impresos.sum()
    totalImpresos = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_resumen_impresos,deletable=False,editable=False,orderby=~db.t_resumen_impresos.f_fecha)
    return dict(form=form,total=totalImpresos)

@auth.requires_membership('estadisticas')
def auditados():
    """
    Gets all the data to display the number of Auditados per day from the resumen_impresos table
    Also shows the total sum of rechazados, aceptados and auditados
    """
    db.t_resumen_auditados.id.readable = False
    query = (db.t_resumen_auditados.f_auditados != 0)
    sum = db.t_resumen_auditados.f_auditados.sum()
    totalAuditados = db(query).select(sum).first()[sum]
    query = (db.t_resumen_auditados.f_aceptados != 0)
    sum = db.t_resumen_auditados.f_aceptados.sum()
    totalAceptados = db(query).select(sum).first()[sum]
    query = (db.t_resumen_auditados.f_rechazados != 0)
    sum = db.t_resumen_auditados.f_rechazados.sum()
    totalRechazados = db(query).select(sum).first()[sum]
    form = SQLFORM.grid(db.t_resumen_auditados,deletable=False,editable=False,orderby=~db.t_resumen_auditados.f_fecha)
    return dict(form=form,total=totalAuditados,aceptados=totalAceptados,rechazados=totalRechazados)

@auth.requires_membership('estadisticas')
def egresados():
    """
    Gets all the data to display the number of Egresados per year from the Egresados table
    """
    db.t_egresados.id.readable = False
    query = (db.t_egresados.f_egresados != 0)
    sum = db.t_egresados.f_egresados.sum()
    totalEgresados = db(query).select(sum).first()[sum]

    form = SQLFORM.grid(db.t_egresados,deletable=False,editable=False,orderby=~db.t_egresados.f_anio)
    return dict(form=form,total=totalEgresados)
