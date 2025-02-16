import serial

def seri_iletisim(port, baudrate, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        return {"success": True, "connection": ser}
    except serial.SerialException as e:
        return {"success": False, "error": f"Seri port hatası: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Beklenmedik hata oluştu: {e}"}

def seri_yaz(ser_dict, veri):
    if not (isinstance(ser_dict, dict) and ser_dict.get("success")):
        return {"success": False, "error": "Geçersiz seri bağlantı. Önce bağlantı kurulmalı."}
    ser = ser_dict["connection"]
    try:
        if isinstance(veri, str):
            ser.write(veri.encode())
        elif isinstance(veri, bytes):
            ser.write(veri)
        else:
            return {"success": False, "error": "Gönderilecek veri string veya bytes tipinde olmalı"}
        return {"success": True, "result": "Veri yazıldı"}
    except serial.SerialException as e:
        return {"success": False, "error": f"Seri port yazma hatası: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Beklenmedik hata oluştu: {e}"}

def seri_oku(ser_dict, boyut=1024):
    if not (isinstance(ser_dict, dict) and ser_dict.get("success")):
        return {"success": False, "error": "Geçersiz seri bağlantı. Önce bağlantı kurulmalı."}
    ser = ser_dict["connection"]
    try:
        veri = ser.read(boyut)
        try:
            decoded = veri.decode()
            return {"success": True, "result": decoded}
        except UnicodeDecodeError:
            return {"success": True, "result": veri}
    except serial.SerialException as e:
        return {"success": False, "error": f"Seri port okuma hatası: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Beklenmedik hata oluştu: {e}"}

def seri_kapat(ser_dict):
    if not (isinstance(ser_dict, dict) and ser_dict.get("success")):
        return {"success": False, "error": "Geçersiz seri bağlantı. Önce bağlantı kurulmalı."}
    ser = ser_dict["connection"]
    try:
        ser.close()
        return {"success": True, "result": "Seri bağlantı kapatıldı"}
    except serial.SerialException as e:
        return {"success": False, "error": f"Seri port kapatma hatası: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Beklenmedik hata oluştu: {e}"}