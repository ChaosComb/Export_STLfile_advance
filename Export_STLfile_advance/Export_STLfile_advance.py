#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, os, datetime

_app : adsk.core.Application = adsk.core.Application.get()
_ui : adsk.core.UserInterface = None
_design = adsk.fusion.Design.cast(_app.activeProduct)

def run(context):
    global _app, _ui, _design

    try:
        folder = 'C:/STLExport/'
        if not (os.path.isdir(folder)):
            os.makedirs(folder)
        
        now = datetime.datetime.now()
        folder = folder + '/' + now.strftime("%Y%m%d_%H%M%S")
        os.makedirs(folder)

        body_info = _app.activeProduct.allComponents[0].bRepBodies
        for body in body_info:
            if body.isVisible:
                exportMgr = adsk.fusion.ExportManager.cast(_design.exportManager)
                stlOptions = exportMgr.createSTLExportOptions(body)
                stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
                stlOptions.filename = folder + '/' + body.name
                exportMgr.execute(stlOptions)
        
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
