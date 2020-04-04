import json
import csv
import urllib.request

CODECS = ['utf-8','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']

PREF_CODES = {
    '01':'北海道',
    '02':'青森県',
    '03':'岩手県',
    '04':'宮城県',
    '05':'秋田県',
    '06':'山形県',
    '07':'福島県',
    '08':'茨城県',
    '09':'栃木県',
    '10':'群馬県',
    '11':'埼玉県',
    '12':'千葉県',
    '13':'東京都',
    '14':'神奈川県',
    '15':'新潟県',
    '16':'富山県',
    '17':'石川県',
    '18':'福井県',
    '19':'山梨県',
    '20':'長野県',
    '21':'岐阜県',
    '22':'静岡県',
    '23':'愛知県',
    '24':'三重県',
    '25':'滋賀県',
    '26':'京都府',
    '27':'大阪府',
    '28':'兵庫県',
    '29':'奈良県',
    '30':'和歌山県',
    '31':'鳥取県',
    '32':'島根県',
    '33':'岡山県',
    '34':'広島県',
    '35':'山口県',
    '36':'徳島県',
    '37':'香川県',
    '38':'愛媛県',
    '39':'高知県',
    '40':'福岡県',
    '41':'佐賀県',
    '42':'長崎県',
    '43':'熊本県',
    '44':'大分県',
    '45':'宮崎県',
    '46':'鹿児島県',
    '47':'沖縄県'
}

#convert CSV data to {lg_code:mesh_codes}
def csvstr_to_dicts(csvstr)->dict:
    parsed_dict = {}
    rows = [row for row in csv.reader(csvstr.splitlines())]
    #header = rows[0]
    maindatas = rows[1:]
    for d in maindatas:
        #空行はスキップ
        if d == []:
            continue

        #pref data setup
        pref_code = d[0][:2]
        pref_meshcodes = []
        try:
            pref_meshcodes = parsed_dict[pref_code]
        except KeyError:
            pass
        pref_name = PREF_CODES[pref_code]
        meshcode = d[2][:4]
        if not meshcode in pref_meshcodes:
            pref_meshcodes.append(meshcode)
        parsed_dict[pref_code] = pref_meshcodes

        #lg data setup
        lg_code = d[0]
        meshcodes = []
        try:
            meshcodes = parsed_dict[lg_code]
        except KeyError:
            pass
        lg_name = d[1]
        meshcode = d[2][:4]
        if not meshcode in meshcodes:
            meshcodes.append(meshcode)
        parsed_dict[d[0]] = meshcodes
    return parsed_dict

def csvstr_to_dicts_prefcodes_to_name(csvstr)->dict:
    parsed_dict = {}
    rows = [row for row in csv.reader(csvstr.splitlines())]
    #header = rows[0]
    maindatas = rows[1:]
    for d in maindatas:
        #空行はスキップ
        if d == []:
            continue

        #lg data setup
        lg_code = d[0]
        try:
            lg_name = parsed_dict[lg_code]
        except KeyError:
            pass
        lg_name = d[1]
        parsed_dict[lg_code] = lg_name
    return parsed_dict

    #デコード出来るまでCODECS内全コーデックでトライする
def decode_csv(csv_data)->str:
    print('csv decoding')
    for codec in CODECS:
        try:
            csv_str = csv_data.decode(codec)
            print('ok:' + codec)
            return csv_str
        except:
            print('ng:' + codec)
            continue
    print('Appropriate codec is not found.')

    #外部のCSVファイルをインポート url=xxxx/xxxx.csv
def import_csv_from(baseurl):    
    integrated_datas = {}

    for i in range(3):
        filename = '01-' + str(i + 1)
        csvurl = baseurl + 'csv/%s.csv'%filename
        request_file = get_file(csvurl)
        f = decode_csv(request_file.read())
        data = csvstr_to_dicts(f)
        integrated_datas.update(data)
    
    for i in range(47):
        filename = str(i + 1).zfill(2)
        if i == 0:
            continue
        csvurl = baseurl + 'csv/%s.csv'%filename
        request_file = get_file(csvurl)
        f = decode_csv(request_file.read())
        data = csvstr_to_dicts(f)
        integrated_datas.update(data)

    return integrated_datas

def get_file(fileurl):
    req = urllib.request.Request(fileurl)
    req.add_header('Referer', 'http://localhost')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36 Edg/79.0.309.65')
    request_file = urllib.request.urlopen(req)
    if not request_file.getcode() == 200:
        print('%s:error')
        return
    return request_file


def export_json(data_dict, filepath='./json/meshcodes.json'):
    with open(filepath, 'w') as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    lgcode_meshcode_dict = import_csv_from('https://www.stat.go.jp/data/mesh/')
    export_json(lgcode_meshcode_dict)
