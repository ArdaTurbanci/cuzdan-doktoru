import streamlit as st
import pandas as pd
import requests
import joblib
import os
import time
import numpy as np

st.set_page_config(page_title="EthVerify", page_icon="☑️")
st.title("☑️ EthVerify")
st.write("Ethereum adresinin dolandırıcılık riskini analiz eder.")

API_KEY = os.environ.get("ETHERSCAN_API_KEY", "")
model = joblib.load("cuzdan_doktoru_model.pkl")
COLUMNS = joblib.load("model_columns.pkl")

def adres_ozellikleri(address, deneme=3):
    url = "https://api.etherscan.io/v2/api"
    a = address.lower()
    
    params = {
        "chainid": 1, "module": "account", "action": "txlist",
        "address": address, "startblock": 0, "endblock": 99999999,
        "page": 1, "offset": 10000, "sort": "asc",
        "apikey": API_KEY
    }
    data = None
    for i in range(deneme):
        try: 
            r = requests.get(url, params=params)
            if r.status_code == 200 and r.json().get("status") == "1":
                data = r.json()["result"]
                break
            time.sleep(1.5)
        except Exception:
            time.sleep(1.5)
            
    if data is None:
        return None
        
    tx = data
    sent = [t for t in tx if t["from"].lower() == a]
    received = [t for t in tx if t.get("to", "").lower() == a]
    sent_degerler = [int(t["value"]) / 1e18 for t in sent]
    rec_degerler = [int(t["value"]) / 1e18 for t in received]
    all_ts = sorted(int(t["timeStamp"]) for t in tx)
    
    hesaplanan_bakiye = sum(int(t["value"]) / 1e18 * (1 if t.get("to", "").lower() == a else -1) for t in tx)
    bakiye = max(0.0, hesaplanan_bakiye)

    return {
        "sent_tnx": len(sent),
        "received_tnx": len(received),
        "total_ether_sent": sum(sent_degerler),
        "total_ether_received": sum(rec_degerler),
        "unique_sent_to_addresses": len(set(t["to"].lower() for t in sent)),
        "unique_received_from_addresses": len(set(t["from"].lower() for t in received)),
        "number_of_created_contracts": sum(1 for t in sent if t["to"] == ""),
        "total_ether_balance": bakiye,
        "avg_val_sent": (sum(sent_degerler) / len(sent)) if sent else 0,
        "max_val_sent": max(sent_degerler) if sent else 0,
        "time_diff_between_first_and_last_(mins)": (all_ts[-1] - all_ts[0]) / 60 if all_ts else 0,
        "max_value_received": max(rec_degerler) if rec_degerler else 0,
        "avg_val_received": (sum(rec_degerler) / len(received)) if received else 0,
        "min_value_received": min(rec_degerler) if rec_degerler else 0,
        "min_val_sent": min(sent_degerler) if sent_degerler else 0,
        "total_transactions_(including_tnx_to_create_contract": len(tx),
        "avg_min_between_received_tnx": float(np.mean(np.diff(sorted(int(t["timeStamp"]) for t in received)) / 60)) if len(received) > 1 else 0,
        "erc20_min_val_rec": 0  
    }

adres = st.text_input("Ethereum adresi yapıştırın:", placeholder="0x...")

if st.button("Analiz Et", type="primary"):
    if not adres.startswith("0x"):
        st.error("Geçerli bir adres girin (0x ile başlamalı)")
    else:
        with st.spinner("Blockchain verisi çekiliyor..."):
            ozellikler = adres_ozellikleri(adres)
            
        if ozellikler is None:
            st.warning("⚠️ Adres bulunamadı veya işlem geçmişi yok")
        else:
            input_df = pd.DataFrame([ozellikler]).reindex(columns=COLUMNS, fill_value=0)
            olasilik = model.predict_proba(input_df)[0][1]
            skor = round(olasilik * 100)
            
            sure_dakika = ozellikler.get("time_diff_between_first_and_last_(mins)", 1)
            if sure_dakika <= 0: sure_dakika = 1
            toplam_gonderilen = ozellikler.get("total_ether_sent", 0)
            dakika_basina_hacim = toplam_gonderilen / sure_dakika
            islem_sayisi = ozellikler.get("total_transactions_(including_tnx_to_create_contract", 1)
            avg_val_sent = ozellikler.get("avg_val_sent", 0)

            aktif_gun = sure_dakika / 1440
            gunluk_islem_orani = islem_sayisi / aktif_gun if aktif_gun > 0 else 0
            
            # 1. Olağanüstü Büyük Vur-Kaç / Soyguncu Filtresi (Ronin vb. için)
            if avg_val_sent > 100 and islem_sayisi < 1000:
                skor = max(skor, 95)
            # 2. Standart Vur-Kaç cüzdan koruması
            elif sure_dakika < 500000 and dakika_basina_hacim > 0.05 and toplam_gonderilen > 1000 and islem_sayisi < 200:
                skor = max(skor, 85)
            # 3. Hem uzun ömürlü hem çok işlemli kurumsal koruma
            elif sure_dakika > 525600 and (islem_sayisi >= 1000 or (islem_sayisi >= 500 and gunluk_islem_orani > 1.0)):
                skor = min(skor, 20)
            
            if skor >= 40:
                st.error(f"🔴 RİSK SKORU: {skor}/100 — DOLANDIRICILIK ŞÜPHELİ")
            elif skor >= 25:
                st.warning(f"🟡 RİSK SKORU: {skor}/100 — ŞÜPHELİ AKTİVİTE / TEMASLI")
            else:
                st.success(f"🟢 RİSK SKORU: {skor}/100 — NORMAL GÖRÜNÜYOR")
                
            if ozellikler["total_transactions_(including_tnx_to_create_contract"] >= 1000:
                st.info("ℹ️ Bilgi: Bu cüzdan çok yüksek sayıda işleme sahip. Analiz kısıtlı işlem geçmişiyle yapılmıştır.")

            st.subheader("📊 Adres İstatistikleri")
            col1, col2, col3 = st.columns(3)
            col1.metric("Gönderilen İşlem", ozellikler["sent_tnx"])
            col2.metric("Alınan İşlem", ozellikler["received_tnx"])
            col3.metric("Benzersiz Alıcı", ozellikler["unique_sent_to_addresses"])
            col1.metric("Toplam Gönderilen", f'{ozellikler["total_ether_sent"]:.2f} ETH')
            col2.metric("Toplam Alınan", f'{ozellikler["total_ether_received"]:.2f} ETH')
            col3.metric("Bakiye (Yaklaşık)", f'{ozellikler["total_ether_balance"]:.2f} ETH')
