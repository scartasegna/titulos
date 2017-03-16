# -*- coding: utf-8 -*-
def cargarAuditados():
    db.t_titulos_auditados.f_cargo.readable = False
    db.t_titulos_auditados.id.readable = False
    query=(db.t_titulos_auditados.f_cargo==auth.user_id)
    form = SQLFORM.smartgrid(db.t_titulos_auditados,onupdate=auth.archive,deletable=False,csv = False,constraints = dict(t_titulos_auditados=query))
    return dict(form=form)
