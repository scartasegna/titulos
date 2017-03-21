# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_membership('manager')
def titulos_manage():
    form = SQLFORM.smartgrid(db.t_titulos_impresos,onupdate=auth.archive)
    return locals()

@auth.requires_membership('manager')
def titulos_resumen():
    form = SQLFORM.grid(db.t_resumen_impresos)
    return dict(form=form)
