# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


# Definiciones básicas
define config.name = "Gatekeeper"
define gui.text_color = "#cf1717"
define _ = renpy.translate_string

# Variables de estado del sistema
default global_search_results = []
default current_site_id = "home"
default history = ["home"]
default deep_mode = False
default active_window = "none" 
default browser_visible = False
default replying_email = None
default browser_minimized = False
default mail_visible = False
default mail_minimized = False
default cmd_visible = False
default cmd_minimized = False
default virus_installed = False
default is_downloading = False
default search_query = ""
# Variables de Misiones y Mail
default current_mission = 0 
default inbox = []
default selected_email_index = -1
default reply_menu_visible = False
default next_mail_time = 0
default waiting_for_mail = False
default pending_mission_code = ""
default downloaded_files = []

# Variables del CMD
default cmd_input = ""
default cmd_history_text = ""
default terminal_log = []
default trace_level = 0
default max_trace = 100

# Coordenadas de ventanas
default browser_x = 350
default browser_y = 40
default mail_x = 50
default mail_y = 100
default cmd_x = 200
default cmd_y = 150

# Imágenes y Transformaciones
image bg desktop = "windows.jpg"
image bg fallback = Solid("#008080")

transform screen_shake_glitch:
    xoffset 0
    choice:
        pause 2.0
    choice:
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 yoffset 5
    repeat