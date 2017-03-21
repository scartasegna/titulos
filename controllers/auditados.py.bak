# -*- coding: utf-8 -*-
@auth.requires_membership('auditados')
def cargarAuditados():
    db.t_titulos_auditados.f_cargo.readable = False
    db.t_titulos_auditados.id.readable = False
    query=(db.t_titulos_auditados.f_cargo==auth.user_id)
    form = SQLFORM.smartgrid(db.t_titulos_auditados,onupdate=auth.archive,deletable=False,csv = False, constraints=dict(t_titulos_auditados=query), onvalidation=yaCargo)
    return dict(form=form)

def yaCargo(form):
    #Si estamos editando un campo
    if (request.args[1] == 'edit'):
        #obtenemos el id del campo a modificar
        idUpdate = request.args[3]
    else:
        #Verificamos que solamente ingresen 1 registro por dia
        now =request.now.date
        r = db(db.t_titulos_auditados.f_fecha==request.now.date).select().first()
        if r != None:
            response.flash = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
            form.errors.f_aceptados = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
