import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
import numpy as np
import os

# Renk paleti
TURUNCU = '#c06c30'
MAVI = '#1f77b4'
KOYU_KAHVE = '#433422'
ARKAPLAN = '#fdfbf7'

# docs/images klasörünü oluştur
os.makedirs('docs/images', exist_ok=True)

def dikw_piramidi():
    """DIKW Piramidi - 4 katmanlı bilgi hiyerarşisi"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor(ARKAPLAN)
    
    # Piramit katmanları (alttan üste)
    # Her katman bir yamuk (trapezoid) veya üçgen
    
    # Katman 1: Veri (Data) - En geniş, en altta
    veri_polygon = Polygon(
        [(1, 1), (9, 1), (8, 3.5), (2, 3.5)],
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2,
        alpha=0.8
    )
    ax.add_patch(veri_polygon)
    ax.text(5, 2.25, 'Veri\n(Data)', ha='center', va='center', 
            fontsize=16, fontweight='bold', color='white')
    
    # Katman 2: Enformasyon (Information)
    enformasyon_polygon = Polygon(
        [(2, 3.5), (8, 3.5), (7, 6), (3, 6)],
        facecolor=TURUNCU,
        edgecolor='black',
        linewidth=2,
        alpha=0.8
    )
    ax.add_patch(enformasyon_polygon)
    ax.text(5, 4.75, 'Enformasyon\n(Information)', ha='center', va='center',
            fontsize=15, fontweight='bold', color='white')
    
    # Katman 3: Bilgi (Knowledge)
    bilgi_polygon = Polygon(
        [(3, 6), (7, 6), (6, 8.25), (4, 8.25)],
        facecolor=KOYU_KAHVE,
        edgecolor='black',
        linewidth=2,
        alpha=0.8
    )
    ax.add_patch(bilgi_polygon)
    ax.text(5, 7.125, 'Bilgi\n(Knowledge)', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    
    # Katman 4: Bilgelik (Wisdom) - En dar, en üstte (üçgen)
    bilgelik_polygon = Polygon(
        [(4, 8.25), (6, 8.25), (5, 9.5)],
        facecolor='#2d1f15',  # Daha koyu ton
        edgecolor='black',
        linewidth=2,
        alpha=0.8
    )
    ax.add_patch(bilgelik_polygon)
    ax.text(5, 8.75, 'Bilgelik\n(Wisdom)', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Başlık
    ax.text(5, 0.3, 'DIKW Piramidi', ha='center', va='center',
            fontsize=18, fontweight='bold', color=KOYU_KAHVE)
    
    plt.savefig('docs/images/dikw_piramidi.png', dpi=150, bbox_inches='tight')
    print("[OK] DIKW Piramidi olusturuldu: docs/images/dikw_piramidi.png")


def dosya_vs_vtys():
    """Dosya Sistemi vs VTYS Karşılaştırması"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.patch.set_facecolor(ARKAPLAN)
    
    # --- SOL TARAF: Dosya Sistemi (Karışık) ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Dosya Sistemi\n(Geleneksel Yaklaşım)', 
                  fontsize=16, fontweight='bold', color=KOYU_KAHVE, pad=20)
    
    # Uygulama A
    app_a_box = FancyBboxPatch(
        (1, 7), 2.5, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2
    )
    ax1.add_patch(app_a_box)
    ax1.text(2.25, 7.75, 'Uygulama\nA', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Uygulama B
    app_b_box = FancyBboxPatch(
        (6.5, 7), 2.5, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2
    )
    ax1.add_patch(app_b_box)
    ax1.text(7.75, 7.75, 'Uygulama\nB', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Dosya A
    file_a_box = FancyBboxPatch(
        (1, 3), 2.5, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=TURUNCU,
        edgecolor='black',
        linewidth=2
    )
    ax1.add_patch(file_a_box)
    ax1.text(2.25, 3.75, 'Dosya\nA', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Dosya B
    file_b_box = FancyBboxPatch(
        (6.5, 3), 2.5, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=TURUNCU,
        edgecolor='black',
        linewidth=2
    )
    ax1.add_patch(file_b_box)
    ax1.text(7.75, 3.75, 'Dosya\nB', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Oklar (karışık bağlantılar)
    arrow1 = FancyArrowPatch((2.25, 7), (2.25, 4.5),
                            arrowstyle='->', mutation_scale=25,
                            color=KOYU_KAHVE, linewidth=2.5)
    ax1.add_patch(arrow1)
    
    arrow2 = FancyArrowPatch((7.75, 7), (7.75, 4.5),
                            arrowstyle='->', mutation_scale=25,
                            color=KOYU_KAHVE, linewidth=2.5)
    ax1.add_patch(arrow2)
    
    # Çarpraz oklar (karışıklığı göstermek için)
    arrow3 = FancyArrowPatch((3, 7), (7, 4.5),
                            arrowstyle='->', mutation_scale=20,
                            color='red', linewidth=1.5, linestyle='--', alpha=0.6)
    ax1.add_patch(arrow3)
    
    arrow4 = FancyArrowPatch((7, 7), (3, 4.5),
                            arrowstyle='->', mutation_scale=20,
                            color='red', linewidth=1.5, linestyle='--', alpha=0.6)
    ax1.add_patch(arrow4)
    
    # Sorun notları
    ax1.text(5, 1.5, '! Veri Tekrari\n! Tutarsizlik Riski\n! Yonetim Zorlugu',
            ha='center', va='center', fontsize=11, color='red',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # --- SAĞ TARAF: VTYS (Düzenli) ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Veritabanı Yönetim Sistemi\n(Modern Yaklaşım)',
                  fontsize=16, fontweight='bold', color=KOYU_KAHVE, pad=20)
    
    # Uygulama A
    app_a2_box = FancyBboxPatch(
        (1, 7.5), 2.5, 1.2,
        boxstyle="round,pad=0.1",
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2
    )
    ax2.add_patch(app_a2_box)
    ax2.text(2.25, 8.1, 'Uygulama\nA', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # Uygulama B
    app_b2_box = FancyBboxPatch(
        (6.5, 7.5), 2.5, 1.2,
        boxstyle="round,pad=0.1",
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2
    )
    ax2.add_patch(app_b2_box)
    ax2.text(7.75, 8.1, 'Uygulama\nB', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    
    # VTYS Motoru (Ortada)
    vtys_box = FancyBboxPatch(
        (3, 4.5), 4, 1.8,
        boxstyle="round,pad=0.15",
        facecolor=KOYU_KAHVE,
        edgecolor='black',
        linewidth=2.5
    )
    ax2.add_patch(vtys_box)
    ax2.text(5, 5.4, 'VTYS Motoru', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    
    # Veritabanı (En altta)
    db_box = FancyBboxPatch(
        (3.5, 1.5), 3, 1.5,
        boxstyle="round,pad=0.15",
        facecolor=TURUNCU,
        edgecolor='black',
        linewidth=2.5
    )
    ax2.add_patch(db_box)
    ax2.text(5, 2.25, 'Veritabanı', ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')
    
    # Düzenli oklar
    arrow_a = FancyArrowPatch((2.25, 7.5), (4.5, 6.3),
                             arrowstyle='->', mutation_scale=25,
                             color='green', linewidth=2.5)
    ax2.add_patch(arrow_a)
    
    arrow_b = FancyArrowPatch((7.75, 7.5), (5.5, 6.3),
                             arrowstyle='->', mutation_scale=25,
                             color='green', linewidth=2.5)
    ax2.add_patch(arrow_b)
    
    arrow_db = FancyArrowPatch((5, 4.5), (5, 3),
                              arrowstyle='->', mutation_scale=25,
                              color='green', linewidth=2.5)
    ax2.add_patch(arrow_db)
    
    # Avantaj notları
    ax2.text(5, 0.5, '+ Merkezi Veri Yonetimi\n+ Veri Butunlugu\n+ Es Zamanli Erisim',
            ha='center', va='center', fontsize=11, color='green',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('docs/images/dosya_vs_vtys.png', dpi=150, bbox_inches='tight')
    print("[OK] Dosya Sistemi vs VTYS karsilastirmasi olusturuldu: docs/images/dosya_vs_vtys.png")


def ansi_sparc_mimari():
    """ANSI/SPARC 3 Katmanlı Mimari"""
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    fig.patch.set_facecolor(ARKAPLAN)
    
    # Başlık
    ax.text(5, 13, 'ANSI/SPARC 3 Katmanlı Mimari', ha='center', va='center',
            fontsize=18, fontweight='bold', color=KOYU_KAHVE)
    
    # Katman 1: Harici Seviye (External Views) - En üstte
    external_box = FancyBboxPatch(
        (1.5, 10), 7, 2,
        boxstyle="round,pad=0.15",
        facecolor=MAVI,
        edgecolor='black',
        linewidth=2.5
    )
    ax.add_patch(external_box)
    ax.text(5, 11, 'Harici Seviye\n(External Views)', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    ax.text(5, 10.3, 'Kullanıcı Görünümleri', ha='center', va='center',
            fontsize=10, style='italic', color='white')
    
    # Katman 2: Kavramsal Seviye (Conceptual Schema)
    conceptual_box = FancyBboxPatch(
        (1.5, 6.5), 7, 2,
        boxstyle="round,pad=0.15",
        facecolor=TURUNCU,
        edgecolor='black',
        linewidth=2.5
    )
    ax.add_patch(conceptual_box)
    ax.text(5, 7.5, 'Kavramsal Seviye\n(Conceptual Schema)', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    ax.text(5, 6.8, 'Mantıksal Yapı', ha='center', va='center',
            fontsize=10, style='italic', color='white')
    
    # Katman 3: Fiziksel Seviye (Internal Schema)
    internal_box = FancyBboxPatch(
        (1.5, 3), 7, 2,
        boxstyle="round,pad=0.15",
        facecolor=KOYU_KAHVE,
        edgecolor='black',
        linewidth=2.5
    )
    ax.add_patch(internal_box)
    ax.text(5, 4, 'Fiziksel Seviye\n(Internal Schema)', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    ax.text(5, 3.3, 'Depolama Yapısı', ha='center', va='center',
            fontsize=10, style='italic', color='white')
    
    # Katman 4: Veritabanı (Disk) - En altta
    db_box = FancyBboxPatch(
        (2, 0.5), 6, 1.5,
        boxstyle="round,pad=0.15",
        facecolor='#8B4513',  # Disk için kahverengi ton
        edgecolor='black',
        linewidth=2.5
    )
    ax.add_patch(db_box)
    ax.text(5, 1.25, 'Veritabanı (Disk)', ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')
    
    # Çift yönlü oklar ve veri bağımsızlığı notları
    
    # Ok 1: External <-> Conceptual (Mantıksal Veri Bağımsızlığı)
    arrow1_down = FancyArrowPatch((4.5, 10), (4.5, 8.5),
                                 arrowstyle='->', mutation_scale=25,
                                 color='darkgreen', linewidth=3)
    ax.add_patch(arrow1_down)
    
    arrow1_up = FancyArrowPatch((5.5, 8.5), (5.5, 10),
                               arrowstyle='->', mutation_scale=25,
                               color='darkgreen', linewidth=3)
    ax.add_patch(arrow1_up)
    
    # Mantıksal Veri Bağımsızlığı notu
    ax.text(8.5, 9.25, 'Mantıksal Veri\nBağımsızlığı', ha='left', va='center',
            fontsize=11, fontweight='bold', color='darkgreen',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor='darkgreen', linewidth=2))
    
    # Ok 2: Conceptual <-> Internal (Fiziksel Veri Bağımsızlığı)
    arrow2_down = FancyArrowPatch((4.5, 6.5), (4.5, 5),
                                 arrowstyle='->', mutation_scale=25,
                                 color='darkblue', linewidth=3)
    ax.add_patch(arrow2_down)
    
    arrow2_up = FancyArrowPatch((5.5, 5), (5.5, 6.5),
                               arrowstyle='->', mutation_scale=25,
                               color='darkblue', linewidth=3)
    ax.add_patch(arrow2_up)
    
    # Fiziksel Veri Bağımsızlığı notu
    ax.text(8.5, 5.75, 'Fiziksel Veri\nBağımsızlığı', ha='left', va='center',
            fontsize=11, fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                     edgecolor='darkblue', linewidth=2))
    
    # Ok 3: Internal <-> Database
    arrow3_down = FancyArrowPatch((4.5, 3), (4.5, 2),
                                 arrowstyle='->', mutation_scale=25,
                                 color=KOYU_KAHVE, linewidth=3)
    ax.add_patch(arrow3_down)
    
    arrow3_up = FancyArrowPatch((5.5, 2), (5.5, 3),
                               arrowstyle='->', mutation_scale=25,
                               color=KOYU_KAHVE, linewidth=3)
    ax.add_patch(arrow3_up)
    
    plt.savefig('docs/images/ansi_sparc_mimari.png', dpi=150, bbox_inches='tight')
    print("[OK] ANSI/SPARC 3 Katmanli Mimari olusturuldu: docs/images/ansi_sparc_mimari.png")


if __name__ == '__main__':
    print("=" * 60)
    print("VTYS Akademik Gorseller Olusturuluyor...")
    print("=" * 60)
    
    # Tüm görselleri oluştur
    dikw_piramidi()
    dosya_vs_vtys() 
    ansi_sparc_mimari()
    
    print("=" * 60)
    print("[OK] Tum gorseller basariyla olusturuldu!")
    print("=" * 60)


def ciz_vtys_mimari_kavramlar():
    # Renk Paleti
    renk_mavi = '#1f77b4'
    renk_turuncu = '#c06c30'
    renk_kahve = '#433422'
    renk_bg = '#fdfbf7'

    # --- GÖRSEL 1: ER Model Temel Bileşenleri ---
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    fig1.patch.set_facecolor(renk_bg)
    ax1.set_facecolor(renk_bg)

    # 1. Varlık (Entity) - Dikdörtgen
    ax1.text(0.2, 0.6, "ÖĞRENCİ", ha="center", va="center", fontsize=12, fontweight='bold', color='white',
             bbox=dict(boxstyle="square,pad=0.5", fc=renk_mavi, ec=renk_kahve, lw=2))
    ax1.text(0.2, 0.3, "VARLIK (Entity)\n(Dikdörtgen)", ha="center", va="center", fontsize=10, color=renk_kahve)

    # 2. İlişki (Relationship) - Eşkenar Dörtgen
    # Matplotlib'de 'diamond' boxstyle olmadığı için Polygon ile çiziyoruz
    p_elmas = plt.Polygon([[0.5, 0.8], [0.65, 0.6], [0.5, 0.4], [0.35, 0.6]], closed=True, 
                          facecolor=renk_turuncu, edgecolor=renk_kahve, lw=2)
    ax1.add_patch(p_elmas)
    ax1.text(0.5, 0.6, "KAYIT", ha="center", va="center", fontsize=10, fontweight='bold', color='white')
    ax1.text(0.5, 0.25, "İLİŞKİ (Relationship)\n(Eşkenar Dörtgen)", ha="center", va="center", fontsize=10, color=renk_kahve)

    # 3. Öznitelik (Attribute) - Elips
    ax1.text(0.8, 0.6, "Ad Soyad", ha="center", va="center", fontsize=10, fontweight='bold', color=renk_kahve,
             bbox=dict(boxstyle="ellipse,pad=0.5", fc="white", ec=renk_kahve, lw=2, linestyle='--'))
    ax1.text(0.8, 0.3, "ÖZNİTELİK (Attribute)\n(Elips)", ha="center", va="center", fontsize=10, color=renk_kahve)

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    ax1.set_title("ER Model Temel Bileşenleri", fontsize=14, color=renk_kahve, pad=10)
    plt.savefig('docs/images/er_model_bilesenleri.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: 2-Katmanlı vs 3-Katmanlı Mimari ---
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(12, 6))
    fig2.patch.set_facecolor(renk_bg)
    
    bbox_pc = dict(boxstyle="round,pad=0.3", fc="white", ec=renk_mavi, lw=2)
    bbox_server = dict(boxstyle="round,pad=0.5", fc=renk_turuncu, ec=renk_kahve, lw=2)
    bbox_db = dict(boxstyle="round,pad=0.8", fc=renk_kahve, ec="black", lw=2) # Veritabanı temsili
    
    # SOL: 2-Katmanlı
    ax2a.set_facecolor(renk_bg)
    ax2a.set_title("2-Katmanlı (Client-Server)", color=renk_kahve, fontweight='bold')
    
    ax2a.text(0.5, 0.8, "İSTEMCİ (Client)\n(Arayüz + İş Mantığı)", ha="center", bbox=bbox_pc)
    ax2a.text(0.5, 0.2, "VERİTABANI\nSUNUCUSU", ha="center", bbox=bbox_db, color="white")
    
    ax2a.annotate("", xy=(0.5, 0.3), xytext=(0.5, 0.7), arrowprops=dict(arrowstyle="<->", lw=2, color=renk_mavi))
    ax2a.text(0.55, 0.5, "SQL / Veri", fontsize=9, color=renk_kahve)
    ax2a.axis('off')

    # SAĞ: 3-Katmanlı
    ax2b.set_facecolor(renk_bg)
    ax2b.set_title("3-Katmanlı (Web/App)", color=renk_kahve, fontweight='bold')

    ax2b.text(0.5, 0.85, "İSTEMCİ (Client)\n(Tarayıcı)", ha="center", bbox=bbox_pc, fontsize=9)
    ax2b.text(0.5, 0.5, "UYGULAMA SUNUCUSU\n(İş Mantığı)", ha="center", bbox=bbox_server, color="white", fontsize=9)
    ax2b.text(0.5, 0.15, "VERİTABANI\nSUNUCUSU", ha="center", bbox=bbox_db, color="white", fontsize=9)

    ax2b.annotate("", xy=(0.5, 0.6), xytext=(0.5, 0.78), arrowprops=dict(arrowstyle="<->", lw=2, color=renk_mavi))
    ax2b.annotate("", xy=(0.5, 0.25), xytext=(0.5, 0.4), arrowprops=dict(arrowstyle="<->", lw=2, color=renk_mavi))
    
    ax2b.text(0.55, 0.7, "HTTP", fontsize=8, color=renk_kahve)
    ax2b.text(0.55, 0.35, "SQL", fontsize=8, color=renk_kahve)

    ax2b.axis('off')
    
    plt.tight_layout()
    plt.savefig('docs/images/mimari_katmanlar.png', dpi=150, bbox_inches='tight')
    plt.close()

# Fonksiyonu çalıştır
ciz_vtys_mimari_kavramlar()

def ciz_er_detaylari():
    import matplotlib.patches as patches
    
    # Renk Paleti
    renk_mavi = '#1f77b4'
    renk_turuncu = '#c06c30'
    renk_kahve = '#433422'
    renk_bg = '#fdfbf7'

    # --- GÖRSEL 1: Nitelik Çeşitleri ---
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    fig1.patch.set_facecolor(renk_bg)
    ax1.set_facecolor(renk_bg)

    # 1. Normal (Basit)
    ax1.text(0.15, 0.7, "TC No", ha="center", va="center", bbox=dict(boxstyle="ellipse", fc="white", ec=renk_kahve))
    ax1.text(0.15, 0.55, "Basit", ha="center", fontsize=9)

    # 2. Türetilen (Kesikli)
    ax1.text(0.4, 0.7, "Yaş", ha="center", va="center", bbox=dict(boxstyle="ellipse", fc="white", ec=renk_kahve, ls="--"))
    ax1.text(0.4, 0.55, "Türetilen\n(Kesikli Çizgi)", ha="center", fontsize=9)

    # 3. Çok Değerli (Çift Elips - Matplotlib hilesi)
    # Dış elips
    e1 = patches.Ellipse((0.65, 0.7), 0.15, 0.1, fc="white", ec=renk_kahve, lw=1)
    # İç elips
    e2 = patches.Ellipse((0.65, 0.7), 0.13, 0.08, fc="white", ec=renk_kahve, lw=1)
    ax1.add_patch(e1)
    ax1.add_patch(e2)
    ax1.text(0.65, 0.7, "Telefon", ha="center", va="center", fontsize=10)
    ax1.text(0.65, 0.55, "Çok Değerli\n(Çift Çizgi)", ha="center", fontsize=9)

    # 4. Birleşik (Ağaç Yapısı)
    ax1.text(0.9, 0.8, "Adres", ha="center", va="center", bbox=dict(boxstyle="ellipse", fc="white", ec=renk_kahve))
    # Dallar
    ax1.plot([0.9, 0.82], [0.76, 0.65], color=renk_kahve, lw=1)
    ax1.plot([0.9, 0.98], [0.76, 0.65], color=renk_kahve, lw=1)
    # Alt nitelikler
    ax1.text(0.82, 0.62, "İl", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="ellipse", fc="white", ec=renk_kahve))
    ax1.text(0.98, 0.62, "İlçe", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="ellipse", fc="white", ec=renk_kahve))
    ax1.text(0.9, 0.5, "Birleşik", ha="center", fontsize=9)

    ax1.set_xlim(0, 1.1)
    ax1.set_ylim(0.4, 0.9)
    ax1.axis('off')
    ax1.set_title("Nitelik (Attribute) Çeşitleri", fontsize=14, color=renk_kahve)
    plt.savefig('docs/images/er_nitelik_cesitleri.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: İlişki Türleri (1:1, 1:N, M:N) ---
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    fig2.patch.set_facecolor(renk_bg)
    ax2.set_facecolor(renk_bg)
    
    box_ent = dict(boxstyle="square,pad=0.3", fc=renk_mavi, ec=renk_kahve)
    
    # Fonksiyon: Küçük ER çizimi
    def draw_rel(x_start, label_rel, l_card, r_card):
        # Sol Varlık
        ax2.text(x_start, 0.5, "A", ha="center", va="center", color="white", bbox=box_ent)
        # Sağ Varlık
        ax2.text(x_start+0.2, 0.5, "B", ha="center", va="center", color="white", bbox=box_ent)
        # İlişki (Elmas)
        p = patches.Polygon([[x_start+0.1, 0.55], [x_start+0.13, 0.5], [x_start+0.1, 0.45], [x_start+0.07, 0.5]], closed=True, fc=renk_turuncu, ec=renk_kahve)
        ax2.add_patch(p)
        # Çizgiler
        ax2.plot([x_start+0.02, x_start+0.07], [0.5, 0.5], color=renk_kahve)
        ax2.plot([x_start+0.13, x_start+0.18], [0.5, 0.5], color=renk_kahve)
        # Kardinalite Yazıları
        ax2.text(x_start+0.05, 0.53, l_card, fontsize=9, color=renk_kahve, fontweight='bold')
        ax2.text(x_start+0.15, 0.53, r_card, fontsize=9, color=renk_kahve, fontweight='bold')
        # Alt Başlık
        ax2.text(x_start+0.1, 0.35, label_rel, ha="center", fontsize=10)

    draw_rel(0.05, "1:1 (Bire-Bir)", "1", "1")
    draw_rel(0.35, "1:N (Bire-Çok)", "1", "N")
    draw_rel(0.65, "M:N (Çoktan-Çoğa)", "M", "N")

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0.2, 0.8)
    ax2.axis('off')
    ax2.set_title("İlişki Kardinaliteleri", fontsize=14, color=renk_kahve)
    plt.savefig('docs/images/er_iliski_turleri.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 3: Zayıf Varlık ---
    fig3, ax3 = plt.subplots(figsize=(8, 3))
    fig3.patch.set_facecolor(renk_bg)
    ax3.set_facecolor(renk_bg)

    # Güçlü Varlık
    ax3.text(0.2, 0.5, "PERSONEL", ha="center", va="center", color="white", bbox=dict(boxstyle="square,pad=0.5", fc=renk_mavi, ec=renk_kahve))
    
    # Tanımlayıcı İlişki (Çift Elmas)
    # Dış
    p_out = patches.Polygon([[0.5, 0.7], [0.6, 0.5], [0.5, 0.3], [0.4, 0.5]], closed=True, fc=renk_turuncu, ec=renk_kahve, lw=1)
    # İç
    p_in = patches.Polygon([[0.5, 0.65], [0.57, 0.5], [0.5, 0.35], [0.43, 0.5]], closed=True, fc=renk_turuncu, ec=renk_kahve, lw=1)
    ax3.add_patch(p_out)
    ax3.add_patch(p_in)

    # Zayıf Varlık (Çift Dikdörtgen)
    # Dış
    r_out = patches.Rectangle((0.75, 0.35), 0.2, 0.3, fc="white", ec=renk_kahve, lw=1)
    # İç
    r_in = patches.Rectangle((0.76, 0.37), 0.18, 0.26, fc="white", ec=renk_kahve, lw=1)
    ax3.add_patch(r_out)
    ax3.add_patch(r_in)
    ax3.text(0.85, 0.5, "BAĞIMLI", ha="center", va="center", color=renk_kahve, fontweight='bold')

    # Bağlantılar
    ax3.plot([0.28, 0.4], [0.5, 0.5], color=renk_kahve, lw=2) # Sol
    ax3.plot([0.6, 0.75], [0.5, 0.5], color=renk_kahve, lw=2, ls="-") # Sağ (Çift çizgi temsili normalde kalın yapılır)

    ax3.set_xlim(0, 1)
    ax3.set_ylim(0.2, 0.8)
    ax3.axis('off')
    ax3.set_title("Zayıf Varlık ve Tanımlayıcı İlişki", fontsize=14, color=renk_kahve)
    plt.savefig('docs/images/er_zayif_varlik.png', dpi=150, bbox_inches='tight')
    plt.close()

ciz_er_detaylari()

def ciz_normalizasyon_gorselleri():
    import matplotlib.patches as patches
    
    # Renk Paleti
    renk_mavi = '#1f77b4'
    renk_turuncu = '#c06c30'
    renk_kahve = '#433422'
    renk_bg = '#fdfbf7'

    # --- GÖRSEL 1: Bağımlılık Türleri (Oklar) ---
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    fig1.patch.set_facecolor(renk_bg)
    ax1.set_facecolor(renk_bg)

    def draw_dependency(x_start, title, dep_type):
        ax1.text(x_start + 0.15, 0.85, title, ha="center", fontsize=10, fontweight='bold', color=renk_kahve)
        
        # Kutular
        props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=renk_kahve)
        
        if dep_type == "partial":
            # Kısmi: (A, B) -> C ama A -> C
            ax1.text(x_start, 0.6, "A", bbox=props, ha="center")
            ax1.text(x_start + 0.1, 0.6, "B", bbox=props, ha="center")
            ax1.text(x_start + 0.3, 0.6, "C", bbox=props, ha="center")
            
            # PK Çerçevesi
            rect = patches.Rectangle((x_start - 0.05, 0.52), 0.2, 0.2, fill=False, edgecolor=renk_mavi, linestyle='--', lw=2)
            ax1.add_patch(rect)
            ax1.text(x_start + 0.05, 0.45, "PK (A, B)", ha="center", fontsize=8, color=renk_mavi)
            
            # Ok (A -> C) - Kısmi
            ax1.annotate("", xy=(x_start + 0.28, 0.65), xytext=(x_start + 0.02, 0.65), 
                         arrowprops=dict(arrowstyle="->", color='red', lw=2, connectionstyle="arc3,rad=-0.5"))
            ax1.text(x_start + 0.15, 0.75, "Kısmi\nBağımlılık", ha="center", fontsize=8, color='red')

        elif dep_type == "transitive":
            # Geçişli: A -> B -> C
            ax1.text(x_start, 0.6, "A (PK)", bbox=props, ha="center")
            ax1.text(x_start + 0.15, 0.6, "B", bbox=props, ha="center")
            ax1.text(x_start + 0.3, 0.6, "C", bbox=props, ha="center")
            
            # Ok A->B
            ax1.annotate("", xy=(x_start + 0.13, 0.6), xytext=(x_start + 0.04, 0.6), arrowprops=dict(arrowstyle="->", color=renk_kahve))
            # Ok B->C
            ax1.annotate("", xy=(x_start + 0.28, 0.6), xytext=(x_start + 0.17, 0.6), arrowprops=dict(arrowstyle="->", color='red', lw=2))
            ax1.text(x_start + 0.22, 0.5, "Geçişli\nBağımlılık", ha="center", fontsize=8, color='red')

    draw_dependency(0.05, "Kısmi Bağımlılık (2NF Sorunu)", "partial")
    draw_dependency(0.55, "Geçişli Bağımlılık (3NF Sorunu)", "transitive")

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    plt.savefig('docs/images/norm_bagimlilik_turleri.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: Normalizasyon Kümeleri (İç İçe Kutular) ---
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    fig2.patch.set_facecolor(renk_bg)
    ax2.set_facecolor(renk_bg)

    # Renkler (Dıştan İçe)
    colors = ['#e3f2fd', '#bbdefb', '#90caf9', '#64b5f6']
    labels = ["1NF\n(Atomik)", "2NF\n(Kısmi Yok)", "3NF\n(Geçişli Yok)", "BCNF\n(Determinant=Key)"]
    sizes = [0.9, 0.7, 0.5, 0.3]

    for i in range(4):
        rect = patches.FancyBboxPatch(((1-sizes[i])/2, (1-sizes[i])/2), sizes[i], sizes[i], 
                                      boxstyle="round,pad=0.02", fc=colors[i], ec=renk_kahve)
        ax2.add_patch(rect)
        # Etiket (Sol üst köşe)
        ax2.text((1-sizes[i])/2 + 0.05, (1-sizes[i])/2 + sizes[i] - 0.08, labels[i], 
                 fontsize=9, fontweight='bold', color=renk_kahve, va="top")

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_title("Normal Formlar Hiyerarşisi", fontsize=12, color=renk_kahve)
    plt.savefig('docs/images/norm_kume_gosterimi.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 3: ER -> Tablo Dönüşümü (M:N) ---
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    fig3.patch.set_facecolor(renk_bg)
    ax3.set_facecolor(renk_bg)

    # Üst Kısım: ER Diyagramı
    ax3.text(0.1, 0.8, "ÖĞRENCİ", bbox=dict(boxstyle="square", fc=renk_mavi, ec="black"), color="white", ha="center")
    ax3.text(0.9, 0.8, "DERS", bbox=dict(boxstyle="square", fc=renk_mavi, ec="black"), color="white", ha="center")
    
    # İlişki
    p_rel = patches.Polygon([[0.5, 0.85], [0.6, 0.8], [0.5, 0.75], [0.4, 0.8]], closed=True, fc=renk_turuncu, ec="black")
    ax3.add_patch(p_rel)
    ax3.text(0.5, 0.8, "KAYIT", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    
    # Çizgiler ve M:N
    ax3.plot([0.18, 0.4], [0.8, 0.8], color="black")
    ax3.plot([0.6, 0.82], [0.8, 0.8], color="black")
    ax3.text(0.25, 0.82, "M", fontsize=10)
    ax3.text(0.75, 0.82, "N", fontsize=10)

    # OK (Dönüşüm)
    ax3.annotate("DÖNÜŞÜM", xy=(0.5, 0.55), xytext=(0.5, 0.7), 
                 arrowprops=dict(arrowstyle="->", color=renk_kahve, lw=2), ha="center")

    # Alt Kısım: Tablolar
    # Tablo 1
    ax3.text(0.15, 0.4, "ÖĞRENCİ TABLOSU\n[ PK: OgrID ]", bbox=dict(boxstyle="round", fc="white", ec="black"), ha="center", fontsize=9)
    # Tablo 3
    ax3.text(0.85, 0.4, "DERS TABLOSU\n[ PK: DersKodu ]", bbox=dict(boxstyle="round", fc="white", ec="black"), ha="center", fontsize=9)
    
    # Ortadaki Junction Table
    ax3.text(0.5, 0.25, "KAYIT TABLOSU (Ara Tablo)\nPK: {OgrID, DersKodu}\nFK1: OgrID\nFK2: DersKodu", 
             bbox=dict(boxstyle="round", fc="#fff3e0", ec=renk_turuncu, lw=2), ha="center", fontsize=10)

    # Oklar (FK Bağlantıları)
    ax3.annotate("", xy=(0.35, 0.25), xytext=(0.15, 0.35), arrowprops=dict(arrowstyle="->", color=renk_mavi, ls="--"))
    ax3.annotate("", xy=(0.65, 0.25), xytext=(0.85, 0.35), arrowprops=dict(arrowstyle="->", color=renk_mavi, ls="--"))

    ax3.set_xlim(0, 1)
    ax3.set_ylim(0.1, 1)
    ax3.axis('off')
    ax3.set_title("Çoka-Çok (M:N) İlişkinin Tabloya Dönüşümü", fontsize=12, color=renk_kahve)
    plt.savefig('docs/images/norm_er_to_tablo.png', dpi=150, bbox_inches='tight')
    plt.close()

ciz_normalizasyon_gorselleri()


def ciz_sql_ve_cebir_v3():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    # Renk Paleti
    renk_mavi = '#e3f2fd'       # Açık Mavi (Arkaplan)
    renk_mavi_koyu = '#1565c0'  # Koyu Mavi (Başlıklar)
    renk_secim = '#ffcc80'      # Turuncu (Vurgu)
    renk_bg = '#fdfbf7'         # Sayfa Arkaplanı
    renk_yazi = '#e65100'       # Turuncu Yazı

    def draw_table(ax, x, y, data, col_labels, title, highlight_rows=None, highlight_cols=None):
        # Tablo Başlığı
        ax.text(x + 0.5 * len(col_labels), y + 0.6, title, ha="center", fontsize=10, fontweight="bold")
        
        # Sütun Başlıkları
        for j, col in enumerate(col_labels):
            rect = patches.Rectangle((x + j, y), 1, 0.4, fc=renk_mavi_koyu, ec="black")
            ax.add_patch(rect)
            ax.text(x + j + 0.5, y + 0.2, col, ha="center", va="center", color="white", fontweight="bold")

        # Veri Satırları
        for i, row in enumerate(data):
            row_y = y - (i + 1) * 0.4
            
            fill_color = "white"
            if highlight_rows and i in highlight_rows:
                fill_color = renk_secim
            
            for j, val in enumerate(row):
                cell_color = fill_color
                if highlight_cols and j in highlight_cols:
                    if not highlight_rows: 
                        cell_color = renk_secim
                    elif highlight_rows and i in highlight_rows: 
                         cell_color = "#ffab40"

                rect = patches.Rectangle((x + j, row_y), 1, 0.4, fc=cell_color, ec="black")
                ax.add_patch(rect)
                ax.text(x + j + 0.5, row_y + 0.2, str(val), ha="center", va="center", color="black", fontsize=9)

    # --- GÖRSEL 1: SEÇME (SELECTION - WHERE) ---
    fig1, ax1 = plt.subplots(figsize=(7, 3.5)) # Genişlik artırıldı
    fig1.patch.set_facecolor(renk_bg)
    ax1.set_facecolor(renk_bg)
    
    data = [[1, "Ali", "IT"], [2, "Ayşe", "HR"], [3, "Can", "IT"], [4, "Ece", "HR"]]
    draw_table(ax1, 0, 2, data, ["ID", "Ad", "Bölüm"], "PERSONEL TABLOSU", highlight_rows=[0, 2])
    
    # Yazı koordinatları düzeltildi (Üst üste binmemesi için)
    ax1.text(3.8, 1.8, r"$\sigma_{Bölüm='IT'}$", fontsize=20, color=renk_yazi, ha="left")
    ax1.text(3.8, 0.8, "Sadece 'IT'\nolan satırlar\nseçildi.", ha="left", va="top", fontsize=10)
    
    ax1.set_xlim(-0.5, 6) # Limit genişletildi
    ax1.set_ylim(-0.5, 3.5)
    ax1.axis('off')
    plt.savefig('docs/images/sql_secme_islemi.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: YANSITMA (PROJECTION - SELECT) ---
    fig2, ax2 = plt.subplots(figsize=(7, 3.5))
    fig2.patch.set_facecolor(renk_bg)
    ax2.set_facecolor(renk_bg)
    
    draw_table(ax2, 0, 2, data, ["ID", "Ad", "Bölüm"], "PERSONEL TABLOSU", highlight_cols=[1, 2])
    
    # Yazı koordinatları düzeltildi
    ax2.text(3.8, 1.8, r"$\pi_{Ad, Bölüm}$", fontsize=20, color="#1565c0", ha="left")
    ax2.text(3.8, 0.8, "Sadece 'Ad' ve\n'Bölüm' sütunları\nalındı.", ha="left", va="top", fontsize=10)
    
    ax2.set_xlim(-0.5, 6)
    ax2.set_ylim(-0.5, 3.5)
    ax2.axis('off')
    plt.savefig('docs/images/sql_yansitma_islemi.png', dpi=150, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 3: BİRLEŞTİRME (JOIN) ---
    # (Değişiklik yok, aynı kalıyor)
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    fig3.patch.set_facecolor(renk_bg)
    ax3.set_facecolor(renk_bg)
    data_A = [[1, "Ali", 10], [2, "Can", 20]]
    data_B = [[10, "IT"], [20, "HR"]]
    draw_table(ax3, 0, 3, data_A, ["ID", "Ad", "BolID"], "TABLO A")
    ax3.text(3.5, 2.5, "+", fontsize=20, ha="center")
    draw_table(ax3, 4, 3, data_B, ["BolID", "BolAd"], "TABLO B")
    ax3.annotate("", xy=(3.5, 1.2), xytext=(3.5, 1.8), arrowprops=dict(arrowstyle="->", lw=2))
    data_res = [[1, "Ali", "IT"], [2, "Can", "HR"]]
    draw_table(ax3, 2, 0.5, data_res, ["ID", "Ad", "BolAd"], "SONUÇ (JOIN)")
    ax3.set_xlim(0, 7)
    ax3.set_ylim(-1.5, 4)
    ax3.axis('off')
    plt.savefig('docs/images/sql_join_mantigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    # --- GÖRSEL 4: KÜME İŞLEMLERİ (DÜZELTİLMİŞ KESİŞİM) ---
    fig4, axs = plt.subplots(1, 3, figsize=(12, 4))
    fig4.patch.set_facecolor(renk_bg)
    
    def draw_venn_fixed(ax, title, mode):
        ax.set_facecolor(renk_bg)
        # İki ana daire
        c1 = patches.Circle((0.35, 0.5), 0.3, fc="none", ec="black", lw=2)
        c2 = patches.Circle((0.65, 0.5), 0.3, fc="none", ec="black", lw=2)
        
        if mode == "union":
            # Birleşim: İkisi de boyalı
            c1_fill = patches.Circle((0.35, 0.5), 0.3, fc=renk_secim, alpha=0.6)
            c2_fill = patches.Circle((0.65, 0.5), 0.3, fc=renk_secim, alpha=0.6)
            ax.add_patch(c1_fill); ax.add_patch(c2_fill)
            
        elif mode == "intersect":
            # KESİŞİM DÜZELTME: Clip Path Tekniği
            # 1. Sağdaki daireyi çiz (Boyalı olarak)
            c_intersect = patches.Circle((0.65, 0.5), 0.3, fc=renk_secim, alpha=0.9) # Koyu boya
            # 2. Soldaki daireyi "Kırpıcı" (Clip) olarak kullan
            clip_circle = patches.Circle((0.35, 0.5), 0.3, transform=ax.transData)
            # 3. Kırpma işlemini uygula: Sadece sol dairenin içinde kalan sağ daire parçası çizilir
            c_intersect.set_clip_path(clip_circle)
            ax.add_patch(c_intersect)
            
        elif mode == "difference":
            # Fark (A - B)
            # A'yı boya
            c1_fill = patches.Circle((0.35, 0.5), 0.3, fc=renk_secim, alpha=0.6)
            ax.add_patch(c1_fill)
            # B'yi beyaz boya (üstüne bindir)
            c2_white = patches.Circle((0.65, 0.5), 0.3, fc=renk_bg, ec="black", lw=0) # Kenarsız beyaz
            ax.add_patch(c2_white)

        # Çerçeveleri en üste tekrar çiz (temiz görünüm için)
        ax.add_patch(c1); ax.add_patch(c2)
        
        ax.text(0.1, 0.85, "A", fontsize=12, fontweight="bold")
        ax.text(0.9, 0.85, "B", fontsize=12, fontweight="bold")
        ax.set_title(title, pad=10)
        ax.axis('off')
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    draw_venn_fixed(axs[0], "A UNION B (Hepsi)", "union")
    draw_venn_fixed(axs[1], "A INTERSECT B (Ortak)", "intersect")
    draw_venn_fixed(axs[2], "A - B (Fark)", "difference")
    
    plt.tight_layout()
    plt.savefig('docs/images/sql_kume_islemleri.png', dpi=150, bbox_inches='tight')
    plt.close()

ciz_sql_ve_cebir_v3()

def ciz_sql_join_venn():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    # Renk Paleti
    renk_bg = '#fdfbf7'
    renk_daire = '#e0e0e0'  # Pasif daire rengi
    renk_aktif = '#42a5f5'  # Seçili alan rengi (Mavi)
    renk_yazi = '#333333'

    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    fig.patch.set_facecolor(renk_bg)

    # Temel Venn Çizim Fonksiyonu
    def draw_venn(ax, title, mode):
        ax.set_facecolor(renk_bg)
        
        # Daire Koordinatları
        x1, y1, r = 0.35, 0.5, 0.3
        x2, y2 = 0.65, 0.5
        
        # 1. Pasif Daireleri Çiz (Alt Katman)
        c1_base = patches.Circle((x1, y1), r, fc=renk_daire, ec='black', lw=2)
        c2_base = patches.Circle((x2, y2), r, fc=renk_daire, ec='black', lw=2)
        ax.add_patch(c1_base)
        ax.add_patch(c2_base)
        
        # 2. Moduna Göre Boyama Yap (Üst Katman)
        if mode == 'inner':
            # Kesişim
            clip_circle = patches.Circle((x1, y1), r, transform=ax.transData)
            c2_fill = patches.Circle((x2, y2), r, fc=renk_aktif, alpha=0.9, ec='black')
            c2_fill.set_clip_path(clip_circle)
            ax.add_patch(c2_fill)
            
        elif mode == 'left':
            # Sol Dairenin Tamamı
            c1_fill = patches.Circle((x1, y1), r, fc=renk_aktif, alpha=0.9, ec='black')
            ax.add_patch(c1_fill)
            # Sağ Dairenin sınırlarını tekrar çiz (üstte kalsın diye)
            c2_border = patches.Circle((x2, y2), r, fc='none', ec='black', lw=2)
            ax.add_patch(c2_border)
            
        elif mode == 'right':
            # Sağ Dairenin Tamamı
            c2_fill = patches.Circle((x2, y2), r, fc=renk_aktif, alpha=0.9, ec='black')
            ax.add_patch(c2_fill)
            c1_border = patches.Circle((x1, y1), r, fc='none', ec='black', lw=2)
            ax.add_patch(c1_border)
            
        elif mode == 'full':
            # Her İkisi
            c1_fill = patches.Circle((x1, y1), r, fc=renk_aktif, alpha=0.9, ec='black')
            c2_fill = patches.Circle((x2, y2), r, fc=renk_aktif, alpha=0.9, ec='black')
            ax.add_patch(c1_fill)
            ax.add_patch(c2_fill)

        # Yazılar
        ax.text(0.1, 0.85, "Table A", fontsize=11, fontweight='bold', color=renk_yazi)
        ax.text(0.9, 0.85, "Table B", fontsize=11, fontweight='bold', color=renk_yazi)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=15, color=renk_yazi)
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    # 4 Türü Çiz
    draw_venn(axs[0], "INNER JOIN\n(Sadece Eşleşenler)", 'inner')
    draw_venn(axs[1], "LEFT JOIN\n(Sol + Eşleşenler)", 'left')
    draw_venn(axs[2], "RIGHT JOIN\n(Sağ + Eşleşenler)", 'right')
    draw_venn(axs[3], "FULL OUTER JOIN\n(Hepsi)", 'full')

    plt.tight_layout()
    plt.savefig('docs/images/sql_join_venn.png', dpi=150, bbox_inches='tight')
    plt.close()

ciz_sql_join_venn()



def ciz_mysql_profesyonel():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import matplotlib.patheffects as path_effects

    # Renk Paleti (Modern & Kurumsal)
    c_bg = '#ffffff'       # Beyaz Arkaplan
    c_blue = '#2962ff'     # Ana Mavi
    c_light_blue = '#e3f2fd'
    c_green = '#00c853'    # Başarı/InnoDB
    c_red = '#d50000'      # Kilit/MyISAM
    c_grey = '#eceff1'     # Pasif Alanlar
    c_text = '#263238'     # Koyu Gri Yazı

    def create_figure(figsize=(10, 6)):
        fig, ax = plt.subplots(figsize=figsize)
        fig.patch.set_facecolor(c_bg)
        ax.set_facecolor(c_bg)
        return fig, ax

    def add_shadow(patch):
        patch.set_path_effects([path_effects.SimpleLineShadow(alpha=0.2, offset=(2, -2)), path_effects.Normal()])

    # --- GÖRSEL 1: MySQL Katmanlı Mimarisi (Server Rack Görünümü) ---
    fig1, ax1 = create_figure((10, 7))

    layers = [
        (0.85, "1. BAĞLANTI KATMANI (Connectors)", "JDBC, ODBC, .NET, PHP, Python, Go, Node.js", '#ff9800'),
        (0.60, "2. SUNUCU KATMANI (MySQL Server)", "Connection Pool | SQL Interface | Parser | Optimizer | Caches", c_blue),
        (0.35, "3. DEPOLAMA MOTORLARI (Pluggable Storage Engines)", "InnoDB (Varsayılan) | MyISAM | Memory | CSV | Archive", '#607d8b'),
        (0.10, "4. DOSYA SİSTEMİ (File System)", "Redo Logs | Undo Logs | Data Files | Index Files | Error Logs", '#455a64')
    ]

    for y, title, sub, color in layers:
        # Ana Kutu
        rect = patches.FancyBboxPatch((0.1, y), 0.8, 0.2, boxstyle="round,pad=0.02,rounding_size=0.05", fc=color, ec="none")
        add_shadow(rect)
        ax1.add_patch(rect)
        # Başlık
        ax1.text(0.5, y + 0.14, title, ha="center", va="center", fontsize=12, fontweight='bold', color='white')
        # Alt Bilgi Kutusu
        rect_sub = patches.FancyBboxPatch((0.15, y+0.03), 0.7, 0.08, boxstyle="round,pad=0.01", fc='white', alpha=0.9)
        ax1.add_patch(rect_sub)
        ax1.text(0.5, y + 0.07, sub, ha="center", va="center", fontsize=9, color=c_text)

    # Bağlantı Okları
    for y in [0.83, 0.58, 0.33]:
        ax1.annotate("", xy=(0.5, y), xytext=(0.5, y + 0.07), arrowprops=dict(arrowstyle="->", color=c_text, lw=2))

    ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.1)
    ax1.axis('off')
    plt.savefig('docs/images/mysql_mimarisi.png', dpi=200, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: Locking (Tablo vs Satır) ---
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(12, 5))
    fig2.patch.set_facecolor(c_bg)

    def draw_grid_prof(ax, title, mode):
        ax.set_facecolor(c_bg)
        ax.set_title(title, fontsize=12, fontweight='bold', pad=15, color=c_text)
        
        # Grid Çizimi
        rows, cols = 5, 4
        for r in range(rows):
            for c in range(cols):
                rect = patches.Rectangle((c, rows-r-1), 1, 1, fc='white', ec='#cfd8dc', lw=1)
                ax.add_patch(rect)

        if mode == 'table': # MyISAM
            overlay = patches.Rectangle((-0.1, -0.1), cols+0.2, rows+0.2, fc=c_red, alpha=0.1, ec=c_red, lw=3, ls='--')
            ax.add_patch(overlay)
            ax.text(cols/2, rows/2, "[X] TABLO KİLİTLİ\n(Tüm işlemler bekler)", ha="center", va="center", fontsize=12, fontweight='bold', color=c_red)
        
        elif mode == 'row': # InnoDB
            # Sadece 3. satırı kilitle
            target_row = 2
            rect = patches.Rectangle((0, rows-target_row-1), cols, 1, fc=c_green, alpha=0.2, ec=c_green, lw=2)
            ax.add_patch(rect)
            ax.text(cols/2, rows-target_row-0.5, "[X] Sadece Bu Satır Kilitli", ha="center", va="center", fontsize=10, fontweight='bold', color='#1b5e20')
            ax.text(cols/2, rows-target_row-1.5, "[OK] Diğer satırlara erişilebilir", ha="center", fontsize=9, color='#1b5e20')

        ax.set_xlim(-0.5, cols+0.5); ax.set_ylim(-0.5, rows+0.5)
        ax.axis('off')

    draw_grid_prof(ax2a, "MyISAM (Tablo Bazlı Kilit)", 'table')
    draw_grid_prof(ax2b, "InnoDB (Satır Bazlı Kilit)", 'row')
    plt.savefig('docs/images/mysql_locking.png', dpi=200, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 3: B-Tree İndeks (Simetrik Ağaç) ---
    fig3, ax3 = create_figure((10, 5))

    def draw_node(x, y, text, bg, parent=None):
        # Gölge
        shadow = patches.FancyBboxPatch((x+0.1, y-0.1), 1.2, 0.6, boxstyle="round,pad=0.1", fc='#b0bec5', alpha=0.3, ec='none')
        ax3.add_patch(shadow)
        # Kutu
        node = patches.FancyBboxPatch((x, y), 1.2, 0.6, boxstyle="round,pad=0.1", fc=bg, ec='#37474f', lw=1.5)
        ax3.add_patch(node)
        ax3.text(x + 0.6, y + 0.3, text, ha="center", va="center", fontweight='bold', fontsize=11)
        
        if parent:
            px, py = parent
            # Çizgi (Arkada kalsın diye zorder düşürdük)
            ax3.plot([x+0.6, px+0.6], [y+0.6, py], color='#546e7a', lw=2, zorder=0)

    # Koordinatlar
    root = (5, 4.5)
    l1_nodes = [(2.5, 2.5, "1-40"), (7.5, 2.5, "41-100")]
    l2_nodes = [(1, 0.5, "10"), (2.5, 0.5, "30"), (4, 0.5, "40")] # Solun çocukları
    l2_nodes_right = [(6, 0.5, "50"), (7.5, 0.5, "60"), (9, 0.5, "90")] # Sağın çocukları

    # Çizim
    draw_node(root[0], root[1], "ROOT", c_light_blue)
    
    for x, y, txt in l1_nodes:
        draw_node(x, y, txt, '#fff9c4', parent=root)
    
    for x, y, txt in l2_nodes:
        draw_node(x, y, txt, '#ffffff', parent=(2.5, 2.5))

    for x, y, txt in l2_nodes_right:
        draw_node(x, y, txt, '#ffffff', parent=(7.5, 2.5))
        
    # Arama Yolu (60'ı bulalım)
    ax3.annotate("", xy=(7.9, 3.2), xytext=(5.8, 4.4), arrowprops=dict(arrowstyle="->", color=c_red, lw=3, ls='--'))
    ax3.annotate("", xy=(8.1, 1.2), xytext=(8.1, 2.4), arrowprops=dict(arrowstyle="->", color=c_red, lw=3, ls='--'))
    
    ax3.text(1, 4.5, "B-TREE YAPISI", fontsize=14, fontweight='bold', color=c_blue)
    ax3.text(1, 4.1, "Hedef: 60", fontsize=12, color=c_red)

    ax3.set_xlim(0, 11); ax3.set_ylim(0, 6)
    ax3.axis('off')
    plt.savefig('docs/images/mysql_btree_index.png', dpi=200, bbox_inches='tight')
    plt.close()

ciz_mysql_profesyonel()




def ciz_plsql_gorselleri():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    # Renk Paleti
    c_bg = '#ffffff'
    c_blue = '#2962ff'
    c_orange = '#ff9800'
    c_green = '#4caf50'
    c_red = '#f44336'
    c_text = '#263238'

    # --- GÖRSEL 1: Stored Procedure Çalışma Mantığı ---
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    fig1.patch.set_facecolor(c_bg)
    
    # Client & Server Kutuları
    ax1.add_patch(patches.FancyBboxPatch((0.05, 0.3), 0.25, 0.4, boxstyle="round,pad=0.05", fc=c_blue, alpha=0.1, ec=c_blue))
    ax1.text(0.175, 0.75, "İSTEMCİ (CLIENT)", ha="center", fontweight='bold')
    
    ax1.add_patch(patches.FancyBboxPatch((0.65, 0.2), 0.3, 0.6, boxstyle="round,pad=0.05", fc=c_orange, alpha=0.1, ec=c_orange))
    ax1.text(0.8, 0.85, "SUNUCU (DATABASE SERVER)", ha="center", fontweight='bold')

    # SP İçeriği (Sunucu tarafında)
    ax1.add_patch(patches.Rectangle((0.7, 0.3), 0.2, 0.4, fc='white', ec=c_text))
    ax1.text(0.8, 0.5, "STORED\nPROCEDURE\n(Derlenmiş SQL)", ha="center", va="center", fontsize=9)

    # Akış Oku
    ax1.annotate("CALL Prosedur(id)", xy=(0.68, 0.5), xytext=(0.3, 0.5), 
                 arrowprops=dict(arrowstyle="->", color=c_blue, lw=2))
    ax1.text(0.48, 0.55, "Ağ Trafiği: Düşük", ha="center", color=c_blue, fontsize=10)

    ax1.set_xlim(0, 1); ax1.set_ylim(0, 1); ax1.axis('off')
    plt.savefig('docs/images/plsql_sp_mantigi.png', dpi=200, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 2: Trigger Zamanlaması (Lifecycle) ---
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    fig2.patch.set_facecolor(c_bg)
    
    steps = ["DML İsteği\n(Insert/Update/Delete)", "BEFORE TRIGGER\n(Doğrulama)", "ASIL İŞLEM\n(Table Write)", "AFTER TRIGGER\n(Loglama/Audit)"]
    colors = [c_text, c_orange, c_blue, c_green]
    
    for i, (txt, clr) in enumerate(zip(steps, colors)):
        ax2.add_patch(patches.FancyBboxPatch((i*0.25+0.02, 0.4), 0.2, 0.2, boxstyle="round,pad=0.02", fc=clr, ec='none'))
        ax2.text(i*0.25+0.12, 0.5, txt, ha="center", va="center", color='white', fontsize=9, fontweight='bold')
        if i < 3:
            ax2.annotate("", xy=((i+1)*0.25+0.02, 0.5), xytext=(i*0.25+0.22, 0.5), arrowprops=dict(arrowstyle="->", color=c_text))

    ax2.set_xlim(0, 1); ax2.set_ylim(0, 1); ax2.axis('off')
    ax2.set_title("Trigger Tetiklenme Sırası", fontsize=12, fontweight='bold', pad=20)
    plt.savefig('docs/images/plsql_trigger_siralamasi.png', dpi=200, bbox_inches='tight')
    plt.close()

    # --- GÖRSEL 3: NEW vs OLD Erişilebilirliği ---
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    fig3.patch.set_facecolor(c_bg)
    
    # Tablo verisi
    col_labels = ["İşlem", "OLD (Eski Hal)", "NEW (Yeni Hal)"]
    table_data = [
        ["INSERT", "[X] Mevcut Değil", "[OK] Eklenecek Veri"],
        ["UPDATE", "[OK] Güncelleme Öncesi", "[OK] Güncelleme Sonrası"],
        ["DELETE", "[OK] Silinen Veri", "[X] Mevcut Değil"]
    ]
    
    the_table = ax3.table(cellText=table_data, colLabels=col_labels, loc='center', cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(11)
    the_table.scale(1.2, 2.5)

    # Renklendirme
    for (row, col), cell in the_table.get_celld().items():
        if row == 0:
            cell.set_facecolor(c_blue)
            cell.get_text().set_color('white')
        elif '[X]' in cell.get_text().get_text():
            cell.set_facecolor('#ffebee')
        elif '[OK]' in cell.get_text().get_text():
            cell.set_facecolor('#e8f5e9')

    ax3.axis('off')
    ax3.set_title("Trigger İçinde NEW ve OLD Kullanımı", fontsize=14, fontweight='bold', pad=30)
    plt.savefig('docs/images/plsql_new_old_tablo.png', dpi=200, bbox_inches='tight')
    plt.close()

ciz_plsql_gorselleri()