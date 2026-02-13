# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper

# Maneja el Chat (Messenger) y la Papelera de Reciclaje.

# --- VARIABLES ---
default chat_visible = False
default chat_minimized = False
default chat_history = []
default chat_sender_name = "Handler_X"
default pending_chat_sound = False
default bin_visible = False
default bin_minimized = False

# Mensajes predefinidos para la Papelera
default bin_files = [
    {"name": _("borrame_ya.txt"), "content": _("No sé qué está pasando. El cursor se mueve solo. He desconectado el ratón y se sigue moviendo.")},
    {"name": _("foto_familiar.jpg"), "content": _("[[ERROR: ARCHIVO CORRUPTO - CABECERA HEXADECIMAL NO VÁLIDA]")},
    {"name": _("lista_compras.txt"), "content": _("- Leche\n- Pan\n- Cinta aislante (mucha)\n- Tapones para oídos (el zumbido no para)")},
    {"name": _("diario_secreto.txt"), "content": _("Buscar a Denise en Ghoogle. No confíes en nadie. Ellos están en todas partes.")},
    {"name": _("instrucciones_instalacion.exe"), "content": _("Alenia tiene mas archivos secretos. Debo encontrarlos en Ghoogle antes de que sea demasiado tarde...")},
]
init python:
    # --- SISTEMA DE CHAT ---
    def receive_chat(sender, message):
        store.chat_sender_name = sender
        # Añadimos el mensaje a la historia
        store.chat_history.append((sender, message))
        
        # Abrimos el chat automáticamente para que sea intrusivo
        store.chat_visible = True
        store.chat_minimized = False
        store.active_window = "chat"
        
        # Sonido de notificación
        renpy.play("audio/chat_ding.wav") # Asegúrate de tener este sonido o usa uno genérico
        renpy.restart_interaction()

    def toggle_chat():
        if store.chat_visible and not store.chat_minimized:
            store.chat_minimized = True
        elif store.chat_visible:
            store.chat_minimized = False
        else:
            store.chat_visible = True
            store.chat_minimized = False
            store.active_window = "chat"
        renpy.restart_interaction()

    # --- SISTEMA DE PAPELERA ---
    def open_bin():
        # Cierra otras ventanas grandes para limpiar
        store.browser_visible = False
        
        if store.bin_visible and not store.bin_minimized:
            store.bin_minimized = True
        elif store.bin_visible:
            store.bin_minimized = False
        else:
            store.bin_visible = True
            store.bin_minimized = False
            store.active_window = "bin"
        renpy.restart_interaction()
        
    def close_bin():
        store.bin_visible = False
        renpy.restart_interaction()

# --- SCREENS ---

# Ventana del Chat (Estilo IRC/Messenger retro)
screen chat_window():
    if chat_visible and not chat_minimized:
        drag:
            drag_name "chat_window"
            xpos 800 ypos 400 draggable True drag_handle (0,0, 300, 20)
            
            frame:
                xsize 300 ysize 250 background "#d0d0d0"
                
                # Barra Título
                frame:
                    xpos 2 ypos 2 xsize 296 ysize 20 background "#008000" # Verde tipo Matrix/Hacker
                    text "DarkWire Messenger" color "#fff" size 12 bold True align (0.05, 0.5)
                    button:
                        xsize 15 ysize 15 background "#fff" align (0.95, 0.5)
                        text "_" color "#000" size 10 bold True align (0.5, 0.5)
                        action Function(toggle_chat)

                # Área de Mensajes
                frame:
                    xpos 5 ypos 25 xsize 290 ysize 180 background "#fff"
                    viewport:
                        scrollbars "vertical" mousewheel True draggable True yinitial 1.0
                        vbox:
                            spacing 5
                            for sender, msg in chat_history:
                                if sender == "Unknown" or sender == "???":
                                    text "{b}[sender]:{/b} [msg]" color "#f00" size 12 font "DejaVuSans.ttf" # Rojo para terror
                                else:
                                    text "{b}[sender]:{/b} [msg]" color "#000" size 12 font "DejaVuSans.ttf"

                # Caja de "Escribir" (Falsa, solo decorativa)
                frame:
                    xpos 5 ypos 210 xsize 290 ysize 30 background "#fff"
                    text "Conexión de solo lectura..." color "#aaa" size 10 align (0.05, 0.5) italic True

# Ventana de Papelera
screen bin_window():
    if bin_visible and not bin_minimized:
        drag:
            drag_name "bin_window"
            xpos 100 ypos 100 draggable True drag_handle (0,0, 400, 30)
            
            frame:
                xsize 400 ysize 300 background "#c0c0c0"
                
                # Barra Título
                frame:
                    xpos 4 ypos 4 xsize 392 ysize 26 background "#000080"
                    text "Papelera de Reciclaje" color "#fff" bold True size 14 align (0.02, 0.5)
                    button:
                        xsize 20 ysize 18 background "#c0c0c0" align (0.98, 0.5)
                        text "X" color "#000" size 12 bold True align (0.5, 0.5)
                        action Function(close_bin)
                
                # Contenido
                frame:
                    xpos 10 ypos 40 xsize 380 ysize 250 background "#fff"
                    vbox:
                        spacing 5
                        if not bin_files:
                            text "(Vacío)" color "#888"
                        else:
                            for f in bin_files:
                                button:
                                    background None xfill True
                                    action Notify(f["content"]) 
                                    hbox:
                                        spacing 10
                                        text "🗑" color "#000" size 14
                                        text f["name"] color "#000" size 14