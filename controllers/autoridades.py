# -*- coding: utf-8 -*-

@auth.requires_membership('autoridades')
def auditados():
    """
    Gets all the data created by user and lets add new data
    Shows all that users had created. Adds also exportable data for an especific user
    """
    db.t_titulos_auditados.id.readable = False
    query=(db.t_titulos_auditados.f_cargo==auth.user_id)
    permisoUsuario=False
    if (auth.user_id == 11):
        permisoUsuario = True
    form = SQLFORM.smartgrid(db.t_titulos_auditados, onupdate=auth.archive, editable = permisoUsuario ,deletable=False, csv = permisoUsuario, onvalidation=yaCargoAuditados,orderby=~db.t_titulos_auditados.f_fecha)
    return dict(form=form)

@auth.requires_membership('autoridades')
def yaCargoAuditados(form):
    if (request.args[1] == 'edit'):
        idUpdate = request.args[3]
    else:
        now =request.now.date
        r = db(db.t_titulos_auditados.f_fecha==request.now.date).select().first()
        if r != None:
            response.flash = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
            form.errors.f_aceptados = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))

@auth.requires_membership('autoridades')
def egresados():
    """
    Gets all the data created by user and lets add new data
    Shows all that users had created.
    """
    db.t_egresados.id.readable = False
    form = SQLFORM.smartgrid(db.t_egresados,onupdate=auth.archive,csv=True,details=False,searchable=False)
    return dict(form=form)

@auth.requires_membership('autoridades')
def impresos():
    """
    Gets all the data created by user and lets add new data
    Shows all that users had created. Adds also exportable data for an especific user
    """
    db.t_titulos_impresos.id.readable = False
    query=(db.t_titulos_impresos.f_cargo==auth.user_id)
    form = SQLFORM.smartgrid(db.t_titulos_impresos,onupdate=auth.archive,csv = True, onvalidation=yaCargoImpresos)
    return dict(form=form)

@auth.requires_membership('autoridades')
def yaCargoImpresos(form):
    if (request.args[1] == 'edit'):
        idUpdate = request.args[3]
    else:
        now =request.now.date
        r = db(db.t_titulos_impresos.f_fecha==request.now.date).select().first()
        if r != None:
            response.flash = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
            form.errors.f_aceptados = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
