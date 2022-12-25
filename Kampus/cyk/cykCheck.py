import util
import checkIndex

RCNFT = {
    "S" : [
        ["programming"],
        ["bola"],
        ["ibu"],
        ["sayur"],
        ["dapur"],
        ["makanan"],
        ["pasar"],
        ["kue"],
        ["toko"],
        ["ojek"],
        ["online"],
        ["sampah"],
        ["lapangan"],
        ["sayur"],
        ["bayam"],
        ["adik"],
        ["obat"],
        ["kakek"],
        ["rumah"],
        ["obat"],
        ["apotek"],
        ["sepeda"],
        ["kota"],
        ["bapak"],
        ["tiket"],
        ["liburan"],
        ["negara"],
        ["piala"],
        ["dunia"],
        ["paman"],
        ["sungai"],
        ["universitas"],
        ["provinsi"],
        ["kota"],
        ["pantai"],
        ["danau"],
        ["pulau"],
        ["jurnal"],
        ["planet"],
        ["yupiter"],
        ["bukit"],
        ["ibu"],
        ["teluk"],
        ["hijau"],
        ["kuda"],
        ["gunung"],
        ["sungai"],
        ["turis"],
        ["lautan"],
        ["teman"],
        ["laut"],
        ["lembah"],
        ["selat"],
        ["wilayah"],
        ["barat"],
        ["perahu"],
        ["dayung"],
        ["danau"],
        ["hari"],
        ["suci"],
        ["galungan"],
        ["bulan"],
        ["januari"],
        ["senin"],
        ["upacara"],
        ["bendera"],
        ["sumpah"],
        ["pemuda"],
        ["tanggal"],
        ["oktober"],
        ["batik"],
        ["nyepi"],
        ["maret"],
        ["adik"],
        ["guru"],
        ["sekolah"],
        ["saraswati"],
        ["pendidikan"],
        ["mei"],
        ["perayaan"],
        ["natal"],
        ["desember"],
        ["mobil"],
        ["ayah"],
        ["buku"],
        ["air"],
        ["hujan"],
        ["sidang"],
        ["skripsi"],
        ["ruang"],
        ["sekolah"],
        ["keluarga"],
        ["makan"],
        ["ikan"],
        ["warung"],
        ["kamar"],
        ["pagar"],
        ["tanaman"],
        ["kemerdekaan"],
        ["agustus"],
        ["ponsel"],
        ["yanto"],
        ["budi"],
        ["wayan"],
        ["tasya"],
        ["andi"],
        ["tono"],
        ["pandu"],
        ["joko"],
        ["wawan"],
        ["diah"],
        ["doni"],
        ["yudi"],
        ["agus"],
        ["farrel"],
        ["bento"],
        ["jakarta"],
        ["singapura"],
        ["tokyo"],
        ["nursini"],
        ["bali"],
        ["palembang"],
        ["bekasi"],
        ["indonesia"],
        ["qatar"],
        ["rina"],
        ["surabaya"],
        ["amerika"],
        ["selatan"],
        ["yuda"],
        ["denpasar"],
        ["udayana"],
        ["bali"],
        ["bandung"],
        ["tabanan"],
        ["yoga"],
        ["jembrana"],
        ["pandawa"],
        ["raka"],
        ["tamblingan"],
        ["jawa"],
        ["bromo"],
        ["kiran"],
        ["aere"],
        ["asia"],
        ["flores"],
        ["jesika"],
        ["kuta"],
        ["serin"],
        ["grand"],
        ["canyon"],
        ["sunda"],
        ["bisma"],
        ["toba"],
        ["dono"],
        ["toni"],
        ["andini"],
        ["liam"],
        ["saya"],
        ["kami"],
        ["aku"],
        ["itu"], 
        
        ["setiap"],
        ["28"],
        ["2"],
        ["dua"],
        ["17"], 
    ],

    "P" : [
        ["belajar"],
        ["bermain"],
        ["memasak"],
        ["membeli"],
        ["memesan"],
        ["membuang"],
        ["lari"],
        ["makan"],
        ["merawat"],
        ["meminum"],
        ["dirawat"],
        ["lahir"],
        ["pergi"],
        ["berlibur"],
        ["bekerja"],
        ["menyukai"],
        ["lahir"],
        ["menonton"],
        ["datang"],
        ["terdapat"],
        ["dilahirkan"],
        ["terletak"],
        ["mengunjungi"],
        ["berasal"],
        ["memancing"],
        ["berasal"],
        ["membaca"],
        ["berfoto"],
        ["menaiki"],
        ["tenggelam"],
        ["berada"],
        ["bercerita"],
        ["berjemur"],
        ["terdapat"],
        ["dilaksanakan"],
        ["diperingati"],
        ["memperingati"],
        ["adalah"],
        ["terkena"],
        ["melakukan"],
        ["makan"],
        ["malam"],
        ["membuat"],
        ["dirayakan"], 
    ],
    "O" : [
        ["programming"],
        ["bola"],
        ["ibu"],
        ["sayur"],
        ["dapur"],
        ["makanan"],
        ["pasar"],
        ["kue"],
        ["toko"],
        ["ojek"],
        ["online"],
        ["sampah"],
        ["lapangan"],
        ["sayur"],
        ["bayam"],
        ["adik"],
        ["obat"],
        ["kakek"],
        ["rumah"],
        ["obat"],
        ["apotek"],
        ["sepeda"],
        ["kota"],
        ["bapak"],
        ["tiket"],
        ["liburan"],
        ["negara"],
        ["piala"],
        ["dunia"],
        ["paman"],
        ["sungai"],
        ["universitas"],
        ["provinsi"],
        ["kota"],
        ["pantai"],
        ["danau"],
        ["pulau"],
        ["jurnal"],
        ["planet"],
        ["yupiter"],
        ["bukit"],
        ["ibu"],
        ["teluk"],
        ["hijau"],
        ["kuda"],
        ["gunung"],
        ["sungai"],
        ["turis"],
        ["lautan"],
        ["teman"],
        ["laut"],
        ["lembah"],
        ["selat"],
        ["wilayah"],
        ["barat"],
        ["perahu"],
        ["dayung"],
        ["danau"],
        ["hari"],
        ["suci"],
        ["galungan"],
        ["bulan"],
        ["januari"],
        ["senin"],
        ["upacara"],
        ["bendera"],
        ["sumpah"],
        ["pemuda"],
        ["tanggal"],
        ["oktober"],
        ["batik"],
        ["nyepi"],
        ["maret"],
        ["adik"],
        ["guru"],
        ["sekolah"],
        ["saraswati"],
        ["pendidikan"],
        ["mei"],
        ["perayaan"],
        ["natal"],
        ["desember"],
        ["mobil"],
        ["ayah"],
        ["buku"],
        ["air"],
        ["hujan"],
        ["sidang"],
        ["skripsi"],
        ["ruang"],
        ["sekolah"],
        ["keluarga"],
        ["makan"],
        ["ikan"],
        ["warung"],
        ["kamar"],
        ["pagar"],
        ["tanaman"],
        ["kemerdekaan"],
        ["agustus"],
        ["ponsel"],
        ["yanto"],
        ["budi"],
        ["wayan"],
        ["tasya"],
        ["andi"],
        ["tono"],
        ["pandu"],
        ["joko"],
        ["wawan"],
        ["diah"],
        ["doni"],
        ["yudi"],
        ["agus"],
        ["farrel"],
        ["bento"],
        ["jakarta"],
        ["singapura"],
        ["tokyo"],
        ["nursini"],
        ["bali"],
        ["palembang"],
        ["bekasi"],
        ["indonesia"],
        ["qatar"],
        ["rina"],
        ["surabaya"],
        ["amerika"],
        ["selatan"],
        ["yuda"],
        ["denpasar"],
        ["udayana"],
        ["bali"],
        ["bandung"],
        ["tabanan"],
        ["yoga"],
        ["jembrana"],
        ["pandawa"],
        ["raka"],
        ["tamblingan"],
        ["jawa"],
        ["bromo"],
        ["kiran"],
        ["aere"],
        ["asia"],
        ["flores"],
        ["jesika"],
        ["kuta"],
        ["serin"],
        ["grand"],
        ["canyon"],
        ["sunda"],
        ["bisma"],
        ["toba"],
        ["dono"],
        ["toni"],
        ["andini"],
        ["liam"],
        ["saya"],
        ["kami"],
        ["aku"],
        ["itu"],

        ["setiap"],
        ["28"],
        ["2"],
        ["dua"],
        ["17"], 
    ],
    "Pel" : [
        ["programming"],
        ["bola"],
        ["ibu"],
        ["sayur"],
        ["dapur"],
        ["makanan"],
        ["pasar"],
        ["kue"],
        ["toko"],
        ["ojek"],
        ["online"],
        ["sampah"],
        ["lapangan"],
        ["sayur"],
        ["bayam"],
        ["adik"],
        ["obat"],
        ["kakek"],
        ["rumah"],
        ["obat"],
        ["apotek"],
        ["sepeda"],
        ["kota"],
        ["bapak"],
        ["tiket"],
        ["liburan"],
        ["negara"],
        ["piala"],
        ["dunia"],
        ["paman"],
        ["sungai"],
        ["universitas"],
        ["provinsi"],
        ["kota"],
        ["pantai"],
        ["danau"],
        ["pulau"],
        ["jurnal"],
        ["planet"],
        ["yupiter"],
        ["bukit"],
        ["ibu"],
        ["teluk"],
        ["hijau"],
        ["kuda"],
        ["gunung"],
        ["sungai"],
        ["turis"],
        ["lautan"],
        ["teman"],
        ["laut"],
        ["lembah"],
        ["selat"],
        ["wilayah"],
        ["barat"],
        ["perahu"],
        ["dayung"],
        ["danau"],
        ["hari"],
        ["suci"],
        ["galungan"],
        ["bulan"],
        ["januari"],
        ["senin"],
        ["upacara"],
        ["bendera"],
        ["sumpah"],
        ["pemuda"],
        ["tanggal"],
        ["oktober"],
        ["batik"],
        ["nyepi"],
        ["maret"],
        ["adik"],
        ["guru"],
        ["sekolah"],
        ["saraswati"],
        ["pendidikan"],
        ["mei"],
        ["perayaan"],
        ["natal"],
        ["desember"],
        ["mobil"],
        ["ayah"],
        ["buku"],
        ["air"],
        ["hujan"],
        ["sidang"],
        ["skripsi"],
        ["ruang"],
        ["sekolah"],
        ["keluarga"],
        ["makan"],
        ["ikan"],
        ["warung"],
        ["kamar"],
        ["pagar"],
        ["tanaman"],
        ["kemerdekaan"],
        ["agustus"],
        ["ponsel"],
        ["yanto"],
        ["budi"],
        ["wayan"],
        ["tasya"],
        ["andi"],
        ["tono"],
        ["pandu"],
        ["joko"],
        ["wawan"],
        ["diah"],
        ["doni"],
        ["yudi"],
        ["agus"],
        ["farrel"],
        ["bento"],
        ["jakarta"],
        ["singapura"],
        ["tokyo"],
        ["nursini"],
        ["bali"],
        ["palembang"],
        ["bekasi"],
        ["indonesia"],
        ["qatar"],
        ["rina"],
        ["surabaya"],
        ["amerika"],
        ["selatan"],
        ["yuda"],
        ["denpasar"],
        ["udayana"],
        ["bali"],
        ["bandung"],
        ["tabanan"],
        ["yoga"],
        ["jembrana"],
        ["pandawa"],
        ["raka"],
        ["tamblingan"],
        ["jawa"],
        ["bromo"],
        ["kiran"],
        ["aere"],
        ["asia"],
        ["flores"],
        ["jesika"],
        ["kuta"],
        ["serin"],
        ["grand"],
        ["canyon"],
        ["sunda"],
        ["bisma"],
        ["toba"],
        ["dono"],
        ["toni"],
        ["andini"],
        ["liam"],
        ["saya"],
        ["kami"],
        ["aku"],
        ["itu"],

        ["setiap"],
        ["28"],
        ["2"],
        ["dua"],
        ["17"], 
    ],
    "Noun" : [
        ["programming"],
        ["bola"],
        ["ibu"],
        ["sayur"],
        ["dapur"],
        ["makanan"],
        ["pasar"],
        ["kue"],
        ["toko"],
        ["ojek"],
        ["online"],
        ["sampah"],
        ["lapangan"],
        ["sayur"],
        ["bayam"],
        ["adik"],
        ["obat"],
        ["kakek"],
        ["rumah"],
        ["obat"],
        ["apotek"],
        ["sepeda"],
        ["kota"],
        ["bapak"],
        ["tiket"],
        ["liburan"],
        ["negara"],
        ["piala"],
        ["dunia"],
        ["paman"],
        ["sungai"],
        ["universitas"],
        ["provinsi"],
        ["kota"],
        ["pantai"],
        ["danau"],
        ["pulau"],
        ["jurnal"],
        ["planet"],
        ["yupiter"],
        ["bukit"],
        ["ibu"],
        ["teluk"],
        ["hijau"],
        ["kuda"],
        ["gunung"],
        ["sungai"],
        ["turis"],
        ["lautan"],
        ["teman"],
        ["laut"],
        ["lembah"],
        ["selat"],
        ["wilayah"],
        ["barat"],
        ["perahu"],
        ["dayung"],
        ["danau"],
        ["hari"],
        ["suci"],
        ["galungan"],
        ["bulan"],
        ["januari"],
        ["senin"],
        ["upacara"],
        ["bendera"],
        ["sumpah"],
        ["pemuda"],
        ["tanggal"],
        ["oktober"],
        ["batik"],
        ["nyepi"],
        ["maret"],
        ["adik"],
        ["guru"],
        ["sekolah"],
        ["saraswati"],
        ["pendidikan"],
        ["mei"],
        ["perayaan"],
        ["natal"],
        ["desember"],
        ["mobil"],
        ["ayah"],
        ["buku"],
        ["air"],
        ["hujan"],
        ["sidang"],
        ["skripsi"],
        ["ruang"],
        ["sekolah"],
        ["keluarga"],
        ["makan"],
        ["ikan"],
        ["warung"],
        ["kamar"],
        ["pagar"],
        ["tanaman"],
        ["kemerdekaan"],
        ["agustus"],
        ["ponsel"]
    ],
    "PropNoun" : [
        ["yanto"],
        ["budi"],
        ["wayan"],
        ["tasya"],
        ["andi"],
        ["tono"],
        ["pandu"],
        ["joko"],
        ["wawan"],
        ["diah"],
        ["doni"],
        ["yudi"],
        ["agus"],
        ["farrel"],
        ["bento"],
        ["jakarta"],
        ["singapura"],
        ["tokyo"],
        ["nursini"],
        ["bali"],
        ["palembang"],
        ["bekasi"],
        ["indonesia"],
        ["qatar"],
        ["rina"],
        ["surabaya"],
        ["amerika"],
        ["selatan"],
        ["yuda"],
        ["denpasar"],
        ["udayana"],
        ["bali"],
        ["bandung"],
        ["tabanan"],
        ["yoga"],
        ["jembrana"],
        ["pandawa"],
        ["raka"],
        ["tamblingan"],
        ["jawa"],
        ["bromo"],
        ["kiran"],
        ["aere"],
        ["asia"],
        ["flores"],
        ["jesika"],
        ["kuta"],
        ["serin"],
        ["grand"],
        ["canyon"],
        ["sunda"],
        ["bisma"],
        ["toba"],
        ["dono"],
        ["toni"],
        ["andini"],
        ["liam"],

        ["saya"],
        ["kami"],
        ["aku"],
        ["itu"], 
    ],
    "Num" : [
        ["setiap"],
        ["28"],
        ["2"],
        ["dua"],
        ["17"], 
    ],
    "Adv" : [
        ["sedang"],
        ["sangat"], 
    ],
    "Verb" : [
        ["belajar"],
        ["bermain"],
        ["memasak"],
        ["membeli"],
        ["memesan"],
        ["membuang"],
        ["lari"],
        ["makan"],
        ["merawat"],
        ["meminum"],
        ["dirawat"],
        ["lahir"],
        ["pergi"],
        ["berlibur"],
        ["bekerja"],
        ["menyukai"],
        ["lahir"],
        ["menonton"],
        ["datang"],
        ["terdapat"],
        ["dilahirkan"],
        ["terletak"],
        ["mengunjungi"],
        ["berasal"],
        ["memancing"],
        ["berasal"],
        ["membaca"],
        ["berfoto"],
        ["menaiki"],
        ["tenggelam"],
        ["berada"],
        ["bercerita"],
        ["berjemur"],
        ["terdapat"],
        ["dilaksanakan"],
        ["diperingati"],
        ["memperingati"],
        ["adalah"],
        ["terkena"],
        ["melakukan"],
        ["malam"],
        ["membuat"],
        ["dirayakan"], 
    ],
    "Adj" : [
        ["sakit"],
        ["khas"],
        ["terpanjang"],
        ["cinta"],
        ["banyak"],
        ["nasional"],
        ["raya"],
        ["baru"],
        ["memesan"],
        ["bakar"],
        ["mahal"], 
        ],
    "Prep" : [
        ["di"],
        ["ke"],
        ["dari"],
        ["tentang"],
        ["pada"], 
    ],
    "NP" : [
        ["programming"], 
        ["bola"], 
        ["ibu"], 
        ["sayur"], 
        ["dapur"], 
        ["makanan"], 
        ["pasar"], 
        ["kue"], 
        ["toko"], 
        ["ojek"], 
        ["online"], 
        ["sampah"], 
        ["lapangan"], 
        ["sayur"], 
        ["bayam"], 
        ["adik"], 
        ["obat"], 
        ["kakek"], 
        ["rumah"], 
        ["obat"], 
        ["apotek"], 
        ["sepeda"], 
        ["kota"], 
        ["bapak"], 
        ["tiket"], 
        ["liburan"], 
        ["negara"], 
        ["piala"], 
        ["dunia"], 
        ["paman"], 
        ["sungai"], 
        ["Universitas"], 
        ["provinsi"], 
        ["kota"], 
        ["pantai"], 
        ["danau"], 
        ["pulau"], 
        ["jurnal"], 
        ["planet"], 
        ["Yupiter"], 
        ["bukit"], 
        ["ibu"], 
        ["teluk"], 
        ["hijau"], 
        ["kuda"], 
        ["gunung"], 
        ["sungai"], 
        ["turis"], 
        ["lautan"], 
        ["teman"], 
        ["laut"], 
        ["lembah"], 
        ["selat"], 
        ["wilayah"], 
        ["barat"], 
        ["perahu"], 
        ["dayung"], 
        ["danau"], 
        ["hari"], 
        ["suci"], 
        ["Galungan"], 
        ["bulan"], 
        ["Januari"], 
        ["Senin"], 
        ["upacara"], 
        ["bendera"], 
        ["sumpah"], 
        ["pemuda"], 
        ["tanggal"], 
        ["Oktober"], 
        ["batik"], 
        ["nyepi"], 
        ["Maret"], 
        ["adik"], 
        ["guru"], 
        ["sekolah"], 
        ["Saraswati"], 
        ["pendidikan"], 
        ["Mei"], 
        ["perayaan"], 
        ["Natal"], 
        ["Desember"], 
        ["mobil"], 
        ["ayah"], 
        ["buku"], 
        ["air"], 
        ["hujan"], 
        ["sidang"], 
        ["skripsi"], 
        ["ruang"],
        ["sekolah"] ,
        ["restoran"],
        ["keluarga"], 
        ["makan"], 
        ["ikan"], 
        ["warung"], 
        ["kamar"], 
        ["pagar"], 
        ["tanaman"], 
        ["kemerdekaan"], 
        ["Agustus"], 
        ["ponsel "], 
        ["saya"], 
        ["kami"], 
        ["aku"], 
        ["itu"], 
        ["yanto"], 
        ["budi"], 
        ["wayan"], 
        ["tasya"], 
        ["andi"], 
        ["tono"], 
        ["pandu"], 
        ["joko"], 
        ["wawan"], 
        ["diah"], 
        ["doni"], 
        ["yudi"], 
        ["agus"], 
        ["farrel"], 
        ["bento"], 
        ["jakarta"], 
        ["singapura"], 
        ["tokyo"], 
        ["nursini"], 
        ["bali"], 
        ["palembang"], 
        ["bekasi"], 
        ["indonesia"], 
        ["qatar"], 
        ["rina"], 
        ["surabaya"], 
        ["amerika"],
        ["selatan"], 
        ["yuda"], 
        ["denpasar"], 
        ["udayana"], 
        ["bali"], 
        ["bandung"], 
        ["tabanan"], 
        ["yoga"], 
        ["jembrana"], 
        ["pandawa"], 
        ["raka"], 
        ["amblingan"], 
        ["jawa"], 
        ["bromo"], 
        ["kiran"], 
        ["aere"], 
        ["asia"], 
        ["flores"], 
        ["jesika"], 
        ["kuta"], 
        ["serin"], 
        ["grand"], 
        ["canyon"], 
        ["sunda"], 
        ["bisma"], 
        ["toba"], 
        ["dono"], 
        ["toni"], 
        ["andini"], 
        ["liam"],
        ["17"], 
        ["setiap"],
        ["28"],
        ["2"],
        ["dua"],
        ["17"], 
    ],
    "VP" : [    
        ["belajar"],
        ["bermain"],
        ["memasak"],
        ["membeli"],
        ["memesan"],
        ["membuang"],
        ["lari"],
        ["makan"],
        ["merawat"],
        ["meminum"],
        ["dirawat"],
        ["lahir"],
        ["pergi"],
        ["berlibur"],
        ["bekerja"],
        ["menyukai"],
        ["lahir"],
        ["menonton"],
        ["datang"],
        ["terdapat"],
        ["dilahirkan"],
        ["terletak"],
        ["mengunjungi"],
        ["berasal"],
        ["memancing"],
        ["berasal"],
        ["membaca"],
        ["berfoto"],
        ["menaiki"],
        ["tenggelam"],
        ["berada"],
        ["bercerita"],
        ["berjemur"],
        ["terdapat"],
        ["dilaksanakan"],
        ["diperingati"],
        ["memperingati"],
        ["adalah"],
        ["terkena"],
        ["melakukan"],
        ["makan"],
        ["malam"],
        ["membuat"],
        ["dirayakan"]
    ]
}

RCNFNT = {   
    "K" : [
        ["K2K1"],
        ["K2O"],
        ["K2K3"],
        ["K2Ket"],
        ["K2Pel"],
        ["SP"]
    ],
    "K1" : [["OKet"]],
    "K2" : [["SP"]],
    "K3" : [["OPel"]],

    "S" : [
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropNoun"],
        ["AdjNP"],
        ["NPPropNoun"],
        ["NounNP"]
    ],
    "P" : [
        ["AdvVerb"],
        ["AdvAdj"]
    ],
    "O" : [
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropNoun"],
        ["AdjNP"],
        ["NPPropNoun"],
        ["NounNP"]
    ],
    "Pel" : [
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropNoun"],
        ["AdjNP"],
        ["NPPropNoun"],
        ["NounNP"],
        ["PrepNP"]
    ],
    "Ket" : [["PrepNP"]],
    "NP" : [ 
        ["NPAdj"], 
        ["NPNoun"], 
        ["NumNP"], 
        ["NPPropnoun"], 
        ["AdjNP"], 
        ["NPPropNoun"], 
        ["NounNP"]
    ],
    "VP" : [
        ["AdvVerb"],
        ["AdvAdj"]
    ]
}

def checkDebug(word) :
    rows = len(word)
    table = util.makeTableDebug(word, rows)

    for i in range(0, rows, 1): 
        for j in range(0, rows - i, 1) : 
            ### exctract dictionary kiri & kanan
            if i == 0 : table = checkIndex.firstIndexDebug(RCNFT, table[i][j], table, i, j)
            if i > 0 : table = checkIndex.otherIndexDebug(i - 1, j, RCNFNT, table, i, j)

        print()
        print()
        util.printTable(table, len(word))
    util.printTable(table, rows)

    if "K" in (table[rows-1][0][0].split()) : return True
    else : return False


def check(word) :
    rows = len(word)
    table = util.makeTable(word, rows)

    for i in range(0, rows, 1): 
        for j in range(0, rows - i, 1) : 
            ### exctract dictionary kiri & kanan
            if i == 0 : table = checkIndex.firstIndex(RCNFT, table[i][j], table, i, j)
            if i > 0 : table = checkIndex.otherIndex(i - 1, j, RCNFNT, table, i, j)

    if "K" in (table[rows-1][0][0].split()) : return True
    else : return False
