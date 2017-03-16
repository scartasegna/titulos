# -*- coding: utf-8 -*-

### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()

@auth.requires_login()
def titulos():
    db.t_titulos.f_cargo.readable = False
    form = SQLFORM.smartgrid(db.t_titulos,onupdate=auth.archive,deletable=False,csv = False,onvalidation=verificar_suma)
    return locals()

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
