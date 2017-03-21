# -*- coding: utf-8 -*-
# intente algo como

@auth.requires_membership('titulos')
def titulos_impresos():
    db.t_titulos_impresos.f_cargo.readable = False
    db.t_titulos_impresos.id.readable = False
    query=(db.t_titulos_impresos.f_cargo==auth.user_id)
    form = SQLFORM.smartgrid(db.t_titulos_impresos,onupdate=auth.archive,deletable=False,csv = False,constraints = dict(t_titulos_impresos=query), onvalidation=yaCargo)
    return dict(form=form)

def yaCargo(form):
    #Si estamos editando un campo
    if (request.args[1] == 'edit'):
        #obtenemos el id del campo a modificar
        idUpdate = request.args[3]
    else:
        #Verificamos que solamente ingresen 1 registro por dia
        now =request.now.date
        r = db(db.t_titulos_impresos.f_fecha==request.now.date).select().first()
        if r != None:
            response.flash = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))
            form.errors.f_aceptados = 'Ya ingreso un registro para la fecha (%s). Por favor actualicelo' % (request.now.date().strftime("%d-%m-%Y"))

def verificar_suma(form):
    regiones = form.vars.f_region1 + form.vars.f_region2 + form.vars.f_region3 + form.vars.f_region4 + form.vars.f_region5
    regiones = regiones + form.vars.f_region6 + form.vars.f_region7 + form.vars.f_region8 + form.vars.f_region9
    regiones = regiones + form.vars.f_region10 + form.vars.f_region11 + form.vars.f_region12 + form.vars.f_region13
    regiones = regiones + form.vars.f_region14 + form.vars.f_region15 + form.vars.f_region16 + form.vars.f_region17
    regiones = regiones + form.vars.f_region18 + form.vars.f_region19 + form.vars.f_region20 + form.vars.f_region21
    regiones = regiones + form.vars.f_region22 + form.vars.f_region23 + form.vars.f_region24 + form.vars.f_region25
    aceptados = form.vars.f_aceptados
    if aceptados < regiones:
        form.errors.f_aceptados = 'La cantidad de aceptados no puede ser menor a la suma de las regiones (%s) ' % (regiones)
