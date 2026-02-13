# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


# Maneja el Rastreo Pasivo, los Virus (Pop-ups) y las Trampas (Honeypots)

# --- VARIABLES ---
default virus_popups = []        # Lista de popups activos en pantalla
default next_virus_spawn = 0     # Temporizador para el siguiente popup
default passive_trace_timer = 0  # Contador interno para el rastreo

init python:
    import random

    def spawn_virus_popup():
        # Solo aparecen si el virus está instalado y NO estamos en "Mi PC" (Refugio)
        if not store.virus_installed: 
            return
        if store.active_window == "mypc": 
            return
        if store.antivirus_timer > 0:
            return

        # Probabilidad de aparición (aumenta con el nivel de rastreo)
        chance = 30 + (store.trace_level / 2) 
        if random.randint(0, 100) < chance:
            
            # Definimos un popup nuevo con posición aleatoria
            new_popup = {
                "id": random.randint(1000, 9999),
                "x": random.randint(100, 700),
                "y": random.randint(50, 400),
                "text": random.choice([
                    _("NO MIRES ATRÁS"), 
                    _("TE VEO"), 
                    _("ERROR CRÍTICO"), 
                    _("SISTEMA COMPROMETIDO"),
                    _("¿ESTÁS SOLO?"),
                    _("ARCHIVOS CORRUPTOS"),
                    _("01001001"),
                    _("ELLOS SABEN DÓNDE VIVES"),
                    _("MANTENTE ALERTA"),
                    _("TU SISTEMA NO ES SEGURO"),
                    _("¡AYUDA!"),
                    _("S.O.S."),
                    _("EL TIEMPO SE ACABA"),
                    _("NO HAY ESCAPE"),
                    _("ESTÁS SIENDO RASTREADO")
                ]),
                "color": random.choice(["#f00", "#000", "#500"])
            }
            store.virus_popups.append(new_popup)
            
            renpy.play("audio/error_popup.wav", channel="sound") 
            renpy.restart_interaction()

    def close_popup(popup_id):
        # Filtramos la lista para quitar el popup que tenga ese ID
        store.virus_popups = [p for p in store.virus_popups if p["id"] != popup_id]
        renpy.restart_interaction()

    def clear_all_popups():
        # Esta es la función para "Mi PC" (Limpieza automática)
        store.virus_popups = []
        renpy.restart_interaction()

    # --- 2. LÓGICA DE RASTREO PASIVO (PRESIÓN DE TIEMPO) ---

    def threat_tick():
        # Esta función se llamará cada 1.0 segundo desde el desktop
        
        # A) RASTREO PASIVO
        # Si estás en Deep Mode y NO estás seguro en "Mi PC"
        if store.deep_mode and store.active_window != "mypc":
            # Sube 1% de rastreo cada 5 segundos (aprox)
            store.passive_trace_timer += 1
            if store.passive_trace_timer >= 5:
                store.passive_trace_timer = 0
                update_trace(1) 
        
        # B) GENERADOR DE VIRUS
        if store.virus_installed and store.active_window != "mypc":
            spawn_virus_popup()
        
        # --- C) CUENTA ATRÁS DEL ANTIVIRUS ---
        if store.antivirus_timer > 0:
            store.antivirus_timer -= 1
            # Si se acaba el tiempo, avisamos al jugador
            if store.antivirus_timer == 0:
                renpy.notify(_("⚠ PROTECCIÓN DE RAM EXPIRADA ⚠"))
                renpy.play("audio/error_buzz.mp3.wav")

# --- 3. PANTALLA VISUAL DE LOS POP-UPS ---
screen virus_layer():
    # Esta pantalla se superpone al escritorio
    if virus_popups:
        for p in virus_popups:
            drag:
                # Los hacemos arrastrables para que sea más caótico/interactivo
                xpos p["x"] ypos p["y"] draggable True
                
                frame:
                    xsize 250 ysize 120 background "#c0c0c0"
                    
                    # Barra de título roja (Virus)
                    frame:
                        xpos 2 ypos 2 xsize 246 ysize 20 background "#f00"
                        text "⚠ WARNING" color "#fff" size 12 bold True align (0.05, 0.5)
                        
                        # Botón Cerrar (X)
                        button:
                            xsize 15 ysize 15 background "#fff" align (0.95, 0.5)
                            text "X" color "#000" size 10 bold True align (0.5, 0.5)
                            action Function(close_popup, p["id"])
                    
                    # Contenido del Popup
                    vbox:
                        align (0.5, 0.6) spacing 5
                        text p["text"] color p["color"] font "DejaVuSans.ttf" size 16 bold True xalign 0.5
                        
                        textbutton _("ACEPTAR"):
                            xalign 0.5
                            text_size 10
                            action Function(close_popup, p["id"])