from woniutest.ui_util  import web_ui
ui=web_ui.UiUtil
setattr(ui,"mmm","9")

if hasattr(ui,"mmm"):
    print(type(getattr(ui,"mmm")))