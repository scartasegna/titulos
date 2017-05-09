# -*- coding: utf-8 -*-
@auth.requires_membership('auditados')
def cargarAuditados():
    """
    Gets all the data created by user and lets add new data
    Shows all that users had created. Adds also exportable data for an especific user
    """
    db.t_titulos_auditados.f_cargo.readable = False
    db.t_titulos_auditados.id.readable = False
    #obtenemos la zona del usuario
    groups = db((db.auth_membership.user_id==auth.user.id) & (db.auth_membership.group_id==db.auth_group.id)).select(db.auth_group.role)
    habilitarZonas(groups)
    query=(db.t_titulos_auditados.f_cargo==auth.user_id)
    form = SQLFORM.smartgrid(db.t_titulos_auditados, onupdate=auth.archive, deletable=False, csv = False, constraints=dict(t_titulos_auditados=query), orderby=~db.t_titulos_auditados.f_fecha, onvalidation=yaCargo)
    return dict(form=form)

def yaCargo(form):
    """
    Checks that all the user has not added a record for the date
    revices the form as param
    """
    if (request.args[1] == 'edit'):
        idUpdate = request.args[3]
    else:
        now =request.now.date
        r = db((db.t_titulos_auditados.f_fecha==request.now.date) & (db.t_titulos_auditados.f_cargo==auth.user_id)).select().first()
        if r != None:
            response.flash = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
            form.errors.f_aceptados = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
    verificar_suma(form)

def verificar_suma(form):
    """
    Checks that all the sum of regionX equals the number of auditados
    revices the form as param
    """
    regiones = (form.vars.f_region1 or 0) + (form.vars.f_region2 or 0) + (form.vars.f_region3 or 0) + (form.vars.f_region4 or 0)
    regiones = regiones + (form.vars.f_region5 or 0) + (form.vars.f_region6 or 0) + (form.vars.f_region7 or 0) + (form.vars.f_region8 or 0)
    regiones = regiones + (form.vars.f_region9 or 0) + (form.vars.f_region10 or 0) + (form.vars.f_region11 or 0) +(form.vars.f_region12 or 0)
    regiones = regiones + (form.vars.f_region13 or 0) + (form.vars.f_region14 or 0) + (form.vars.f_region15 or 0) + (form.vars.f_region16 or 0)
    regiones = regiones + (form.vars.f_region17 or 0) + (form.vars.f_region18 or 0) + (form.vars.f_region19 or 0) + (form.vars.f_region20 or 0)
    regiones = regiones + (form.vars.f_region21 or 0) + (form.vars.f_region22 or 0) + (form.vars.f_region23 or 0) + (form.vars.f_region24 or 0)
    regiones = regiones + (form.vars.f_region25 or 0)
    aceptados = form.vars.f_aceptados
    rechazados = form.vars.f_rechazados
    total = aceptados + rechazados
    if total != regiones:
        form.errors.f_aceptados = 'La cantidad de Audtidatos (%s) no puede ser distinto a la suma de las regiones (%s) ' % (total,regiones)

def habilitarZonas(groups):
    """
    Defines the records to show according to the zona that the user has assigned
    """
    for group in groups:
        #zona1
        if group.role =='zona1':
            db.t_titulos_auditados.f_region1.readable = False
            db.t_titulos_auditados.f_region1.writable = False
            db.t_titulos_auditados.f_region3.readable = False
            db.t_titulos_auditados.f_region3.writable = False
            db.t_titulos_auditados.f_region5.readable = False
            db.t_titulos_auditados.f_region5.writable = False
            db.t_titulos_auditados.f_region6.readable = False
            db.t_titulos_auditados.f_region6.writable = False
            db.t_titulos_auditados.f_region7.readable = False
            db.t_titulos_auditados.f_region7.writable = False
            db.t_titulos_auditados.f_region8.readable = False
            db.t_titulos_auditados.f_region8.writable = False
            db.t_titulos_auditados.f_region10.readable = False
            db.t_titulos_auditados.f_region10.writable = False
            db.t_titulos_auditados.f_region11.readable = False
            db.t_titulos_auditados.f_region11.writable = False
            db.t_titulos_auditados.f_region12.readable = False
            db.t_titulos_auditados.f_region12.writable = False
            db.t_titulos_auditados.f_region13.readable = False
            db.t_titulos_auditados.f_region13.writable = False
            db.t_titulos_auditados.f_region16.readable = False
            db.t_titulos_auditados.f_region16.writable = False
            db.t_titulos_auditados.f_region17.readable = False
            db.t_titulos_auditados.f_region17.writable = False
            db.t_titulos_auditados.f_region18.readable = False
            db.t_titulos_auditados.f_region18.writable = False
            db.t_titulos_auditados.f_region19.readable = False
            db.t_titulos_auditados.f_region19.writable = False
            db.t_titulos_auditados.f_region22.readable = False
            db.t_titulos_auditados.f_region22.writable = False
            db.t_titulos_auditados.f_region23.readable = False
            db.t_titulos_auditados.f_region23.writable = False
            #zona2
        if group.role =='zona2':
            db.t_titulos_auditados.f_region2.readable = False
            db.t_titulos_auditados.f_region2.writable = False
            db.t_titulos_auditados.f_region3.readable = False
            db.t_titulos_auditados.f_region3.writable = False
            db.t_titulos_auditados.f_region4.readable = False
            db.t_titulos_auditados.f_region4.writable = False
            db.t_titulos_auditados.f_region7.readable = False
            db.t_titulos_auditados.f_region7.writable = False
            db.t_titulos_auditados.f_region8.readable = False
            db.t_titulos_auditados.f_region8.writable = False
            db.t_titulos_auditados.f_region9.readable = False
            db.t_titulos_auditados.f_region9.writable = False
            db.t_titulos_auditados.f_region12.readable = False
            db.t_titulos_auditados.f_region12.writable = False
            db.t_titulos_auditados.f_region13.readable = False
            db.t_titulos_auditados.f_region13.writable = False
            db.t_titulos_auditados.f_region14.readable = False
            db.t_titulos_auditados.f_region14.writable = False
            db.t_titulos_auditados.f_region15.readable = False
            db.t_titulos_auditados.f_region15.writable = False
            db.t_titulos_auditados.f_region17.readable = False
            db.t_titulos_auditados.f_region17.writable = False
            db.t_titulos_auditados.f_region18.readable = False
            db.t_titulos_auditados.f_region18.writable = False
            db.t_titulos_auditados.f_region19.readable = False
            db.t_titulos_auditados.f_region19.writable = False
            db.t_titulos_auditados.f_region20.readable = False
            db.t_titulos_auditados.f_region20.writable = False
            db.t_titulos_auditados.f_region23.readable = False
            db.t_titulos_auditados.f_region23.writable = False
            db.t_titulos_auditados.f_region24.readable = False
            db.t_titulos_auditados.f_region24.writable = False
            db.t_titulos_auditados.f_region25.readable = False
            db.t_titulos_auditados.f_region25.writable = False
        #Zona3
        if group.role =='zona3':
            db.t_titulos_auditados.f_region1.readable = False
            db.t_titulos_auditados.f_region1.writable = False
            db.t_titulos_auditados.f_region2.readable = False
            db.t_titulos_auditados.f_region2.writable = False
            db.t_titulos_auditados.f_region3.readable = False
            db.t_titulos_auditados.f_region3.writable = False
            db.t_titulos_auditados.f_region5.readable = False
            db.t_titulos_auditados.f_region5.writable = False
            db.t_titulos_auditados.f_region6.readable = False
            db.t_titulos_auditados.f_region6.writable = False
            db.t_titulos_auditados.f_region8.readable = False
            db.t_titulos_auditados.f_region8.writable = False
            db.t_titulos_auditados.f_region11.readable = False
            db.t_titulos_auditados.f_region11.writable = False
            db.t_titulos_auditados.f_region13.readable = False
            db.t_titulos_auditados.f_region13.writable = False
            db.t_titulos_auditados.f_region14.readable = False
            db.t_titulos_auditados.f_region14.writable = False
            db.t_titulos_auditados.f_region15.readable = False
            db.t_titulos_auditados.f_region15.writable = False
            db.t_titulos_auditados.f_region16.readable = False
            db.t_titulos_auditados.f_region16.writable = False
            db.t_titulos_auditados.f_region17.readable = False
            db.t_titulos_auditados.f_region17.writable = False
            db.t_titulos_auditados.f_region18.readable = False
            db.t_titulos_auditados.f_region18.writable = False
            db.t_titulos_auditados.f_region21.readable = False
            db.t_titulos_auditados.f_region21.writable = False
            db.t_titulos_auditados.f_region22.readable = False
            db.t_titulos_auditados.f_region22.writable = False
            db.t_titulos_auditados.f_region24.readable = False
            db.t_titulos_auditados.f_region24.writable = False
        #Zona4
        if group.role =='zona4':
            db.t_titulos_auditados.f_region2.readable = False
            db.t_titulos_auditados.f_region2.writable = False
            db.t_titulos_auditados.f_region4.readable = False
            db.t_titulos_auditados.f_region4.writable = False
            db.t_titulos_auditados.f_region5.readable = False
            db.t_titulos_auditados.f_region5.writable = False
            db.t_titulos_auditados.f_region7.readable = False
            db.t_titulos_auditados.f_region7.writable = False
            db.t_titulos_auditados.f_region9.readable = False
            db.t_titulos_auditados.f_region9.writable = False
            db.t_titulos_auditados.f_region12.readable = False
            db.t_titulos_auditados.f_region12.writable = False
            db.t_titulos_auditados.f_region13.readable = False
            db.t_titulos_auditados.f_region13.writable = False
            db.t_titulos_auditados.f_region14.readable = False
            db.t_titulos_auditados.f_region14.writable = False
            db.t_titulos_auditados.f_region15.readable = False
            db.t_titulos_auditados.f_region15.writable = False
            db.t_titulos_auditados.f_region16.readable = False
            db.t_titulos_auditados.f_region16.writable = False
            db.t_titulos_auditados.f_region17.readable = False
            db.t_titulos_auditados.f_region17.writable = False
            db.t_titulos_auditados.f_region18.readable = False
            db.t_titulos_auditados.f_region18.writable = False
            db.t_titulos_auditados.f_region19.readable = False
            db.t_titulos_auditados.f_region19.writable = False
            db.t_titulos_auditados.f_region20.readable = False
            db.t_titulos_auditados.f_region20.writable = False
            db.t_titulos_auditados.f_region21.readable = False
            db.t_titulos_auditados.f_region21.writable = False
            db.t_titulos_auditados.f_region23.readable = False
            db.t_titulos_auditados.f_region23.writable = False
            db.t_titulos_auditados.f_region24.readable = False
            db.t_titulos_auditados.f_region24.writable = False
            db.t_titulos_auditados.f_region25.readable = False
            db.t_titulos_auditados.f_region25.writable = False
