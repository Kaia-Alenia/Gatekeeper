# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper

# ESTE SCRIPT GENERA SONIDOS RETRO (8-BIT) AUTOMÁTICAMENTE SI NO EXISTEN.
# No necesitas descargar nada más.

init python:
    import wave
    import math
    import struct
    import os

    # Función para crear un tono (Onda Cuadrada para sonido retro)
    def create_beep(filename, duration=0.1, freq=440, vol=0.5):
        # Ruta completa: game/audio/nombre_archivo
        path = os.path.join(config.gamedir, "audio", filename)
        
        # Si el archivo ya existe, no hacemos nada (para no sobrescribir tus audios)
        if os.path.exists(path):
            return

        # Configuración del archivo WAV
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        
        try:
            with wave.open(path, 'w') as wav_file:
                wav_file.setnchannels(1) # Mono
                wav_file.setsampwidth(2) # 16-bit
                wav_file.setframerate(sample_rate)
                
                # Generar datos de audio
                for i in range(n_samples):
                    # Fórmula de Onda Cuadrada (Square Wave) para sonido 8-bit
                    t = float(i) / sample_rate
                    # Alternamos entre valor positivo y negativo
                    val = 32767.0 * vol if (math.sin(2 * math.pi * freq * t) > 0) else -32767.0 * vol
                    
                    # Escribir el frame
                    data = struct.pack('<h', int(val))
                    wav_file.writeframesraw(data)
                
            print(f"SFX GENERADO: {filename}")
        except Exception as e:
            print(f"Error generando SFX: {e}")

    # --- GENERACIÓN DE LOS SONIDOS FALTANTES ---
    # Se ejecuta al iniciar el juego
    
    # 1. CLICK DE MOUSE (Agudo y muy corto)
    create_beep("click.wav", duration=0.05, freq=1200, vol=0.3)

    # 2. POP-UP DE VIRUS (Tono grave de advertencia)
    create_beep("error_popup.wav", duration=0.2, freq=150, vol=0.6)

    # 3. CHAT DING (Tono agudo tipo Messenger)
    create_beep("chat_ding.wav", duration=0.3, freq=2000, vol=0.4)

    # 4. ALARMA DEL FINAL (Sirena oscilante simple - Tono continuo agudo)
    create_beep("alarm.wav", duration=1.0, freq=880, vol=0.8)